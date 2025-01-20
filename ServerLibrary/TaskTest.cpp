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
    // TaskManager �ʱ�ȭ
    TaskManager::getInstance();

    // SystemReport �ν��Ͻ� ����
    SystemReport systemReport;

    // 1�ʸ��� CPU�� �޸� ��뷮�� �����ϵ��� TaskManager�� �߰�
    const int MONITOR_REPORTING_SEC = 1;
    TaskManager::getInstance().add(&systemReport, MONITOR_REPORTING_SEC, TICK_INFINITY);



    return 0;
}
