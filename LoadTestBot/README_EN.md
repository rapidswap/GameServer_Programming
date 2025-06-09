# Chat Server Load Test Bot (English)

**Advanced Chat Server Load Testing Tool** developed in Python. Supports everything from basic load testing to progressive load increase and adaptive automatic testing.

## 🚀 Quick Start

### ✨ **Progressive Load Test (Recommended)**
```bash
# Simple execution
run_progressive_test.bat

# Or direct execution
python progressive_test.py --scenario 2  # Basic load test
```

### Required Package Installation
```bash
pip install psutil
```

## 📈 Test Results (Verified Working!)

### ✅ Connection Test Results
```
=== Simple Chat Server Connection Test ===
Connecting to server...
Connection successful!
Registering name...
Name packet size: 27 bytes
Chat message sending...
Chat packet size: 46 bytes
Server response received: 16 bytes
Packet length: 16
Decrypted packet type: 145
User list packet received
User count: 0
```

### ✅ Load Test Results  
```
================================================================================
Load Test Status - 2025-06-09 22:45:16
================================================================================
Test time: 10.0s
Bot status: 3/3 connected
Messages: sent 4, received 12
Error count: 0
Throughput: 0.4 messages/sec
```

## 🎯 Progressive Load Test Scenarios

| # | Scenario | Pattern | Bots | Description |
|---|----------|---------|------|-------------|
| 1 | Warm-up Test | Linear | 1→10 | Basic performance check |
| 2 | Basic Load Test | Step | 5→50 | General load testing |
| 3 | Exponential Growth | Exponential | 1→64 | Fast limit detection |
| 4 | Spike Test | Sudden | 10→100 | Burst load response |
| 5 | Ramp Up/Down | Increase/Decrease | 5→40→5 | Load change adaptation |
| 6 | Sustained Load | Sustained | 20 bots | Stability testing |
| 7 | Stress Test | To Limit | 10→200 | Maximum throughput detection |

## 🤖 Adaptive Auto Test

Real-time performance monitoring with automatic load adjustment.

### Performance Thresholds
```python
CPU Usage: ≤ 80%
Memory Usage: ≤ 85%  
Response Time: ≤ 1000ms
Success Rate: ≥ 95%
Error Rate: ≤ 5%
```

### Execution Methods
```bash
# Basic execution
python adaptive_load_tester.py

# Detailed settings
python adaptive_load_tester.py --initial-bots 10 --max-bots 200 --duration 1800
```

## 🛠️ Execution Methods

### A. Batch Scripts (Easiest)
```bash
run_progressive_test.bat    # Progressive load test
run_loadtest.bat           # Basic load test  
run_monitor.bat            # Server monitoring
run_quick_test.bat         # Quick connection test
```

### B. Command Line
```bash
# Basic load test (5→50 bots, increase by 5)
python progressive_test.py --scenario 2

# Custom test
python progressive_test.py --start-bots 1 --max-bots 30 --step-size 3 --step-duration 45

# Adaptive auto test
python adaptive_load_tester.py --initial-bots 5 --max-bots 100
```

### C. Interactive Mode
```bash
python progressive_test.py --interactive

# Available commands:
# list     - List scenarios
# run 2    - Run scenario 2  
# custom   - Custom scenario
# status   - Current status
# report   - Progress report
# export   - Export results
# stop     - Stop test
```

## 📊 Key Features

### Bot Client
- Automatic name registration
- Random chat message sending (3-8 sec intervals)
- Periodic ping testing (30 sec intervals)
- Connection retry logic
- Statistics collection and reporting

### Test Manager
- Multi-bot creation and management
- Gradual connection (server load prevention)
- Real-time statistics monitoring
- JSON format result export
- Broadcast message functionality

### Server Monitoring
- Process-specific resource usage tracking
- System-wide performance monitoring
- Network I/O statistics
- Real-time connection count tracking

## 🔧 Technical Features

### Protocol Compatibility
- **100% Compatible with C# Server**
- Packet encryption/obfuscation support
- XOR-based security protocol
- Identical to production environment

### Performance Analysis
- **Maximum stable concurrent users**: Maximum bots processable without errors
- **Response time changes**: Latency patterns with load increase
- **Throughput limits**: Maximum messages processable per second
- **Resource usage patterns**: CPU/memory usage patterns
- **Failure threshold**: Point where service degradation begins

## 🚀 Recommended Usage Scenarios

### Stage 1: Initial Test
```bash
# Warm-up test for basic performance check
python progressive_test.py --scenario 1
```

### Stage 2: General Load Test
```bash
# Basic load test for main performance metrics
python progressive_test.py --scenario 2
```

### Stage 3: Limit Detection
```bash
# Stress test for maximum throughput
python progressive_test.py --scenario 7
```

### Stage 4: Optimization
```bash
# Adaptive test for optimal concurrent user detection
python adaptive_load_tester.py --max-bots 50
```

## 🔧 Troubleshooting

### Connection Failure
1. Check server status: `netstat -an | findstr :9200`
2. Review firewall settings
3. Check concurrent connection limits
4. Analyze server logs

### Performance Issues
1. System resource monitoring: `python server_monitor.py`
2. Network status check
3. Database performance verification
4. Server process log analysis

## 🏆 Conclusion

This load testing tool allows you to **accurately identify your server's true performance and limits**. Choose from basic tests to advanced adaptive tests based on your requirements.

### **Recommended Starting Method**
```bash
# 1. Simple start
run_progressive_test.bat

# 2. Select warm-up test (1)
# 3. Continue after checking results
# 4. Experience various scenarios
```

**Now verify your server's real performance with systematic and professional load testing!** 🚀

---

## 📁 File Structure

```
LoadTestBot/
├── progressive_test.py           # Progressive load test runner ⭐
├── adaptive_load_tester.py       # Adaptive auto test ⭐
├── run_progressive_test.bat      # One-click execution script ⭐
├── PROGRESSIVE_TEST_GUIDE.md     # Detailed guide ⭐
├── progressive_load_tester.py    # Progressive test manager
├── main.py                       # Basic load test runner
├── load_test_manager.py         # Basic load test manager
├── chat_bot_client.py           # Individual bot client
├── packets.py                   # Packet classes (with encryption)
├── packet_util.py               # Packet utilities
├── packet_types.py              # Packet type definitions
├── packet_obfuscation.py        # Packet encryption/decryption
├── server_monitor.py            # Server monitoring tool
├── simple_test.py               # Simple connection test
├── run_loadtest.bat             # Basic load test execution
├── run_monitor.bat              # Server monitoring execution
├── run_quick_test.bat           # Quick connection test
├── requirements.txt             # Required packages
└── README.md                    # This file
```
