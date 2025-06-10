#!/usr/bin/env python3
"""
성능 분석 및 벤치마크 도구
"""

import time
import threading
from datetime import datetime
from load_test_manager import LoadTestManager


class PerformanceBenchmark:
    """성능 벤치마크 클래스"""
    
    def __init__(self):
        self.results = []
        
    def run_benchmark(self, bot_counts: list, duration_per_test: int = 120):
        """다양한 봇 수로 성능 벤치마크"""
        print("🏆 채팅서버 성능 벤치마크 시작!")
        print("="*60)
        
        for bot_count in bot_counts:
            print(f"\n🧪 테스트: {bot_count}개 봇 ({duration_per_test}초)")
            print("-" * 40)
            
            result = self.test_bot_count(bot_count, duration_per_test)
            self.results.append(result)
            
            self.print_test_result(result)
            
            # 다음 테스트 전 잠깐 대기
            if bot_count != bot_counts[-1]:
                print("⏳ 다음 테스트 준비 중... (10초 대기)")
                time.sleep(10)
        
        # 최종 벤치마크 결과
        self.print_benchmark_summary()
    
    def test_bot_count(self, bot_count: int, duration: int) -> dict:
        """특정 봇 수로 성능 테스트"""
        try:
            manager = LoadTestManager("localhost", 9200)
            manager.create_bots(bot_count)
            manager.start_test(duration)
            
            # 연결 완료 대기
            time.sleep(min(30, bot_count // 5))
            
            # 성능 측정 시작
            start_time = time.time()
            latencies = []
            message_counts = []
            
            # 테스트 기간 동안 성능 측정
            measurement_start = time.time()
            while time.time() - measurement_start < duration - 30:
                time.sleep(10)  # 10초마다 측정
                
                stats = manager.get_current_stats()
                if stats['latency']:
                    latencies.append(stats['latency']['avg'])
                message_counts.append(stats['messages_sent'])
            
            # 최종 통계
            final_stats = manager.get_current_stats()
            manager.stop_test()
            
            return {
                'bot_count': bot_count,
                'duration': duration,
                'connected_bots': final_stats['connected_bots'],
                'success_rate': (final_stats['connected_bots'] / bot_count) * 100,
                'avg_latency': sum(latencies) / len(latencies) if latencies else 0,
                'min_latency': min(latencies) if latencies else 0,
                'max_latency': max(latencies) if latencies else 0,
                'total_messages': final_stats['messages_sent'],
                'messages_per_second': final_stats['messages_sent'] / duration if duration > 0 else 0,
                'error_count': final_stats['error_count'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            return {
                'bot_count': bot_count,
                'error': str(e),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    def print_test_result(self, result: dict):
        """테스트 결과 출력"""
        if 'error' in result:
            print(f"❌ {result['bot_count']}개 봇 테스트 실패: {result['error']}")
            return
        
        print(f"📊 {result['bot_count']}개 봇 성능 결과:")
        print(f"   🔗 연결 성공률: {result['success_rate']:.1f}%")
        print(f"   ⚡ 평균 응답시간: {result['avg_latency']:.1f}ms")
        print(f"   📈 응답시간 범위: {result['min_latency']:.1f}ms ~ {result['max_latency']:.1f}ms")
        print(f"   💬 초당 메시지: {result['messages_per_second']:.1f} msg/s")
        print(f"   ❌ 오류 수: {result['error_count']}")
        
        # 성능 등급
        avg_latency = result['avg_latency']
        if avg_latency < 20:
            grade = "🏆 최고급"
        elif avg_latency < 40:
            grade = "⭐ 우수"
        elif avg_latency < 80:
            grade = "✅ 양호"
        else:
            grade = "⚠️ 개선필요"
        
        print(f"   🎯 성능 등급: {grade}")
    
    def print_benchmark_summary(self):
        """벤치마크 요약 결과"""
        print("\n" + "="*60)
        print("🏆 최종 성능 벤치마크 결과")
        print("="*60)
        
        successful_results = [r for r in self.results if 'error' not in r]
        
        if not successful_results:
            print("❌ 성공한 테스트가 없습니다.")
            return
        
        # 봇 수별 성능 표
        print(f"{'봇 수':>6} | {'성공률':>7} | {'응답시간':>8} | {'처리량':>10} | {'등급':>8}")
        print("-" * 55)
        
        for result in successful_results:
            bot_count = result['bot_count']
            success_rate = result['success_rate']
            latency = result['avg_latency']
            throughput = result['messages_per_second']
            
            # 등급 결정
            if latency < 20:
                grade = "최고급"
            elif latency < 40:
                grade = "우수"
            elif latency < 80:
                grade = "양호"
            else:
                grade = "개선필요"
            
            print(f"{bot_count:>6} | {success_rate:>6.1f}% | {latency:>6.1f}ms | {throughput:>8.1f}/s | {grade:>8}")
        
        # 권장 동접자 수
        best_latency = min(r['avg_latency'] for r in successful_results)
        best_result = next(r for r in successful_results if r['avg_latency'] == best_latency)
        
        print(f"\n📈 성능 분석:")
        print(f"   🏆 최고 성능: {best_result['bot_count']}개 봇에서 {best_latency:.1f}ms")
        
        # 실용적 권장 수치
        practical_results = [r for r in successful_results if r['avg_latency'] < 50 and r['success_rate'] > 90]
        if practical_results:
            max_practical = max(r['bot_count'] for r in practical_results)
            print(f"   💡 권장 동접자: 최대 {max_practical}명 (50ms 이하, 90% 이상 성공률)")
        
        # 확장성 예측
        if len(successful_results) >= 2:
            # 선형 증가 가정으로 예측
            last_result = successful_results[-1]
            if last_result['avg_latency'] < 100:
                predicted_500 = (last_result['avg_latency'] / last_result['bot_count']) * 500
                predicted_1000 = (last_result['avg_latency'] / last_result['bot_count']) * 1000
                
                print(f"   🔮 확장성 예측:")
                print(f"      500명: 약 {predicted_500:.0f}ms")
                print(f"      1000명: 약 {predicted_1000:.0f}ms")
        
        print("="*60)


def main():
    """성능 벤치마크 실행"""
    print("🏆 채팅서버 성능 벤치마크를 시작합니다!")
    print()
    
    # 테스트할 봇 수 설정
    bot_counts = [10, 25, 50, 75, 100]
    
    print(f"📋 테스트 계획: {bot_counts} 개 봇")
    print("⏱️  각 테스트: 2분간 진행")
    print("📊 측정 항목: 응답시간, 성공률, 처리량")
    print()
    
    confirm = input("벤치마크를 시작하시겠습니까? (y/n): ")
    if confirm.lower() != 'y':
        print("벤치마크를 취소했습니다.")
        return
    
    # 벤치마크 실행
    benchmark = PerformanceBenchmark()
    try:
        benchmark.run_benchmark(bot_counts, duration_per_test=120)
    except KeyboardInterrupt:
        print("\n\n⚠️ 벤치마크가 중단되었습니다.")
    except Exception as e:
        print(f"\n❌ 벤치마크 오류: {e}")
    
    print("\n👋 성능 벤치마크가 완료되었습니다!")


if __name__ == "__main__":
    main()
