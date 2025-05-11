#pragma once
#include "stdafx.h"

class SendBuffer {
private:
    static const size_t INITIAL_SIZE = 4096;  // 초기 버퍼 크기
    static const size_t THRESHOLD = 1024;     // 전송 임계값

    std::vector<char> buffer_;
    size_t currentSize_;
    std::mutex mutex_;

public:
    SendBuffer() : currentSize_(0) {
        buffer_.resize(INITIAL_SIZE);
    }

    // 패킷 추가 후 임계값 초과 시 true 반환
    bool addPacket(Packet* packet) {
        std::lock_guard<std::mutex> lock(mutex_);

        // 스트림 객체 생성 및 패킷 인코딩
        Stream stream;
        packet->encode(stream);

        size_t packetSize = stream.size();

        // 버퍼 공간 확보
        if (currentSize_ + packetSize > buffer_.size()) {
            buffer_.resize(currentSize_ + packetSize);
        }

        // Stream 클래스의 data() 메서드를 사용하여 데이터 복사
        memcpy(buffer_.data() + currentSize_, stream.data(), packetSize);
        currentSize_ += packetSize;

        // 임계값 초과 시 플러시 신호
        return currentSize_ >= THRESHOLD;
    }

    // 버퍼 내용 소켓으로 전송
    int flush(SOCKET socket) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (currentSize_ == 0) return 0;

        int sent = send(socket, reinterpret_cast<const char*>(buffer_.data()), static_cast<int>(currentSize_), 0);
        if (sent > 0) {
            // 전송된 데이터 제거
            if (static_cast<size_t>(sent) < currentSize_) {
                // 일부만 전송된 경우, 나머지 데이터를 버퍼 앞으로 이동
                memmove(buffer_.data(), buffer_.data() + sent, currentSize_ - sent);
                currentSize_ -= sent;
            }
            else {
                // 모두 전송된 경우
                currentSize_ = 0;
            }
        }
        return sent;
    }

    // 현재 버퍼에 있는 데이터 크기
    size_t size() const {
        return currentSize_;
    }

    // 버퍼 데이터 포인터 반환
    const char* data() const {
        return reinterpret_cast<const char*>(buffer_.data());
    }

    void clear() {
        std::lock_guard<std::mutex> lock(mutex_);
        currentSize_ = 0;
    }
};