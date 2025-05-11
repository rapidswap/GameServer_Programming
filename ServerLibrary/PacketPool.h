#pragma once

#include "stdafx.h"
#include "PacketClass.h"

class PacketPool {
private:
    static const size_t INITIAL_POOL_SIZE = 1000;
    static const size_t EXPAND_SIZE = 500;

    std::vector<Packet*> pool_;
    std::mutex poolLock_;

public:
    PacketPool() {
        ExpandPool(INITIAL_POOL_SIZE);
    }

    ~PacketPool() {
        for (auto packet : pool_) {
            delete packet;
        }
        pool_.clear();
    }

    Packet* AcquirePacket() {
        std::lock_guard<std::mutex> lock(poolLock_);

        if (pool_.empty()) {
            ExpandPool(EXPAND_SIZE);
        }

        Packet* packet = pool_.back();
        pool_.pop_back();
        packet->Reset(); // 재사용 전 상태 초기화
        return packet;
    }

    void ReleasePacket(Packet* packet) {
        if (!packet) return;

        std::lock_guard<std::mutex> lock(poolLock_);
        pool_.push_back(packet);
    }

private:
    void ExpandPool(size_t size) {
        for (size_t i = 0; i < size; ++i) {
            pool_.push_back(new Packet());
        }
    }
};

// 전역 인스턴스를 Singleton으로 제공
typedef Singleton<PacketPool> PacketPoolManager;