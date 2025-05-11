#pragma once
#include "stdafx.h"

class SendBuffer {
private:
    static const size_t INITIAL_SIZE = 4096;  // �ʱ� ���� ũ��
    static const size_t THRESHOLD = 1024;     // ���� �Ӱ谪

    std::vector<char> buffer_;
    size_t currentSize_;
    std::mutex mutex_;

public:
    SendBuffer() : currentSize_(0) {
        buffer_.resize(INITIAL_SIZE);
    }

    // ��Ŷ �߰� �� �Ӱ谪 �ʰ� �� true ��ȯ
    bool addPacket(Packet* packet) {
        std::lock_guard<std::mutex> lock(mutex_);

        // ��Ʈ�� ��ü ���� �� ��Ŷ ���ڵ�
        Stream stream;
        packet->encode(stream);

        size_t packetSize = stream.size();

        // ���� ���� Ȯ��
        if (currentSize_ + packetSize > buffer_.size()) {
            buffer_.resize(currentSize_ + packetSize);
        }

        // Stream Ŭ������ data() �޼��带 ����Ͽ� ������ ����
        memcpy(buffer_.data() + currentSize_, stream.data(), packetSize);
        currentSize_ += packetSize;

        // �Ӱ谪 �ʰ� �� �÷��� ��ȣ
        return currentSize_ >= THRESHOLD;
    }

    // ���� ���� �������� ����
    int flush(SOCKET socket) {
        std::lock_guard<std::mutex> lock(mutex_);
        if (currentSize_ == 0) return 0;

        int sent = send(socket, reinterpret_cast<const char*>(buffer_.data()), static_cast<int>(currentSize_), 0);
        if (sent > 0) {
            // ���۵� ������ ����
            if (static_cast<size_t>(sent) < currentSize_) {
                // �Ϻθ� ���۵� ���, ������ �����͸� ���� ������ �̵�
                memmove(buffer_.data(), buffer_.data() + sent, currentSize_ - sent);
                currentSize_ -= sent;
            }
            else {
                // ��� ���۵� ���
                currentSize_ = 0;
            }
        }
        return sent;
    }

    // ���� ���ۿ� �ִ� ������ ũ��
    size_t size() const {
        return currentSize_;
    }

    // ���� ������ ������ ��ȯ
    const char* data() const {
        return reinterpret_cast<const char*>(buffer_.data());
    }

    void clear() {
        std::lock_guard<std::mutex> lock(mutex_);
        currentSize_ = 0;
    }
};