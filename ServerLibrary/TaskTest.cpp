#include "pch.h"

class SystemReport : public Work
{
public:
    void tick() override
    {
        Monitoring& monitor = Monitoring::getInstance();
        SLog(L"### CPU Usage: %2.2f%%, Memory Usage: %u bytes", monitor.processCpuUsage(), monitor.processMemUsage());
    }
};

int main()
{
    // TaskManager 초기화
    TaskManager::getInstance();

    // SystemReport 인스턴스 생성
    SystemReport systemReport;

    // 1초마다 CPU와 메모리 사용량을 보고하도록 TaskManager에 추가
    const int MONITOR_REPORTING_SEC = 1;
    TaskManager::getInstance().add(&systemReport, MONITOR_REPORTING_SEC, TICK_INFINITY);



    return 0;
}
