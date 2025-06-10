#!/usr/bin/env python3
"""
100개 봇 지속 대화 테스트 - 무한 채팅 모드
"""

import time
import signal
import sys
import threading
import random
from datetime import datetime
from load_test_manager import LoadTestManager


class Persistent100BotTest:
    """100개 봇 지속 대화 테스트 클래스"""
    
    def __init__(self):
        self.manager = None
        self.test_running = False
        self.setup_signal_handlers()
        
        # 다양한 대화 주제와 메시지
        self.conversation_topics = {
            "greetings": [
                "안녕하세요! 좋은 하루입니다! ☀️",
                "반갑습니다~ 오늘 날씨가 좋네요!",
                "안녕! 모두들 잘 지내시죠? 😊",
                "하이~ 새로운 하루가 시작됐어요!",
                "좋은 아침이에요! (또는 좋은 저녁!) 🌅"
            ],
            "gaming": [
                "이번 주말에 새로운 게임 해보실 분?",
                "요즘 어떤 게임하고 계세요?",
                "멀티플레이어 게임 함께 할까요? 🎮",
                "레벨업 축하드려요! 대단하네요!",
                "보스전이 정말 어렵더라구요... 😅"
            ],
            "daily_life": [
                "오늘 점심 뭐 드셨어요?",
                "커피 한 잔의 여유... ☕",
                "주말 계획 있으신가요?",
                "오늘 하루도 고생 많으셨어요!",
                "집에서 넷플릭스 보는 중... 📺"
            ],
            "weather": [
                "비가 와서 시원해졌네요 🌧️",
                "햇살이 정말 좋아요!",
                "눈이 올 것 같은 날씨네요 ❄️",
                "바람이 선선해서 좋네요~",
                "날씨가 변덕스러워요 🌤️"
            ],
            "encouragement": [
                "오늘도 화이팅! 💪",
                "힘내세요! 응원합니다!",
                "다들 수고하고 계시네요!",
                "좋은 일만 가득하길 바라요~ ✨",
                "파이팅! 우리 모두 할 수 있어요!"
            ],
            "random_thoughts": [
                "갑자기 떠오른 생각인데...",
                "혹시 이런 경험 있으신가요?",
                "문득 궁금한 게 있는데요",
                "제 생각에는... 🤔",
                "다들 어떻게 생각하세요?"
            ],
            "reactions": [
                "와 정말요? 대박! 😲",
                "오~ 신기하네요!",
                "그러게요! 맞아맞아!",
                "아하! 그런 거였군요!",
                "ㅋㅋㅋ 재밌네요! 😂"
            ],
            "server_test": [
                "서버 성능 테스트 중입니다~ 📊",
                "동시접속 테스트 진행 중! 🔧",
                "부하테스트 봇 열심히 일하는 중... 🤖",
                "서버 안정성 확인 중입니다!",
                "실시간 채팅 테스트! 메시지가 잘 전달되나요?"
            ]
        }
        
        # 봇별 개성 설정
        self.bot_personalities = {}
    
    def setup_signal_handlers(self):
        """시그널 핸들러 설정 (Ctrl+C 처리)"""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """시그널 핸들러"""
        print("\n\n중단 신호 감지됨. 100개 봇을 안전하게 종료합니다...")
        self.stop_test()
        sys.exit(0)
    
    def setup_bot_personalities(self):
        """봇별 개성 설정"""
        personality_types = [
            {"type": "친근한", "topics": ["greetings", "encouragement", "daily_life"], "frequency": 0.7},
            {"type": "게이머", "topics": ["gaming", "reactions", "encouragement"], "frequency": 0.8},
            {"type": "관찰자", "topics": ["random_thoughts", "weather", "daily_life"], "frequency": 0.5},
            {"type": "응원단", "topics": ["encouragement", "reactions", "greetings"], "frequency": 0.9},
            {"type": "테스터", "topics": ["server_test", "random_thoughts", "reactions"], "frequency": 0.6}
        ]
        
        for i in range(1, 101):  # 1-100번 봇
            personality = random.choice(personality_types)
            self.bot_personalities[i] = {
                "type": personality["type"],
                "preferred_topics": personality["topics"],
                "chat_frequency": personality["frequency"],
                "last_message_time": 0,
                "message_count": 0
            }
    
    def get_bot_message(self, bot_id: int) -> str:
        """봇의 개성에 맞는 메시지 생성"""
        personality = self.bot_personalities.get(bot_id, {
            "preferred_topics": ["greetings"],
            "type": "기본"
        })
        
        # 선호하는 주제에서 랜덤 선택
        topic = random.choice(personality["preferred_topics"])
        messages = self.conversation_topics[topic]
        base_message = random.choice(messages)
        
        # 봇 정보를 가끔 추가 (20% 확률)
        if random.random() < 0.2:
            bot_info = f" (Bot #{bot_id:03d})"
            base_message += bot_info
        
        # 메시지 번호를 가끔 추가 (10% 확률)
        personality["message_count"] += 1
        if random.random() < 0.1:
            base_message += f" [msg#{personality['message_count']}]"
        
        return base_message
    
    def print_banner(self):
        """테스트 시작 배너 출력"""
        print("="*80)
        print("         🤖💬 100개 봇 지속 대화 테스트 💬🤖")
        print("="*80)
        print(f"시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("서버: localhost:9200")
        print("봇 수: 100개")
        print("모드: 무한 대화 (종료하지 않음)")
        print("연결 방식: 5개씩 배치로 안전하게")
        print("대화 특징:")
        print("  • 다양한 주제의 자연스러운 대화")
        print("  • 봇별 개성과 대화 스타일")
        print("  • 5-15초 간격으로 지속적 채팅")
        print("  • 실시간 상태 모니터링")
        print("종료: Ctrl+C (안전한 종료)")
        print("="*80)
    
    def start_persistent_chat(self):
        """100개 봇 지속 대화 시작"""
        try:
            self.print_banner()
            
            # 봇 개성 설정
            print("🎭 봇 개성 설정 중...")
            self.setup_bot_personalities()
            print("✅ 100개 봇의 개성이 설정되었습니다!")
            
            # 로드테스트 매니저 생성
            print("📡 서버 연결 준비 중...")
            self.manager = LoadTestManager(server_host="localhost", server_port=9200)
            
            # 100개 봇 생성 (지속 대화용 설정)
            print("🤖 100개 대화봇 생성 중...")
            if not self.manager.create_bots(100):
                print("❌ 봇 생성 실패!")
                return False
            
            # 각 봇의 메시지 간격을 지속 대화용으로 조정
            self.setup_persistent_chat_bots()
            
            print("✅ 100개 대화봇 생성 완료!")
            print("📋 연결 시작...")
            
            # 무한 테스트 시작 (종료하지 않음)
            print("🚀 지속 대화 테스트 시작...")
            if not self.manager.start_test(0):  # 0 = 무한
                print("❌ 테스트 시작 실패!")
                return False
            
            self.test_running = True
            print("✅ 지속 대화가 시작되었습니다!")
            
            # 연결 진행 상황 모니터링
            self.monitor_connection_progress()
            
            # 지속적 모니터링 시작
            self.start_continuous_monitoring()
            
            return True
            
        except Exception as e:
            print(f"❌ 테스트 실행 중 오류 발생: {e}")
            return False
        finally:
            self.cleanup()
    
    def setup_persistent_chat_bots(self):
        """지속 대화용 봇 설정"""
        for bot in self.manager.bots:
            bot_id = bot.bot_id
            personality = self.bot_personalities.get(bot_id, {})
            
            # 개성에 따른 메시지 간격 설정
            frequency = personality.get("chat_frequency", 0.5)
            if frequency > 0.8:  # 수다쟁이
                bot.message_interval = random.uniform(5.0, 10.0)
            elif frequency > 0.6:  # 보통
                bot.message_interval = random.uniform(8.0, 15.0)
            else:  # 과묵한
                bot.message_interval = random.uniform(15.0, 25.0)
            
            # 사용자 정의 메시지 함수 오버라이드
            bot.get_custom_message = lambda: self.get_bot_message(bot_id)
    
    def monitor_connection_progress(self):
        """연결 진행 상황 모니터링"""
        print("\n📶 100개 봇 연결 진행 상황...")
        
        # 최대 2분 동안 연결 모니터링
        for i in range(120):
            if not self.test_running:
                break
                
            stats = self.manager.get_current_stats()
            connected = stats['connected_bots']
            total = stats['total_bots']
            errors = stats['error_count']
            
            progress = (connected / total) * 100 if total > 0 else 0
            
            print(f"🔗 연결 진행: {connected}/{total} ({progress:.1f}%) | 오류: {errors}개", end='\r')
            
            # 90% 이상 연결되면 성공으로 간주
            if connected >= total * 0.9:
                print(f"\n🎉 연결 완료! {connected}/{total} 봇이 연결되었습니다!")
                break
                
            time.sleep(1)
        
        if self.test_running:
            stats = self.manager.get_current_stats()
            print(f"\n📊 최종 연결 결과: {stats['connected_bots']}/{stats['total_bots']} 봇 연결됨")
            
            if stats['connected_bots'] >= 80:
                print("✅ 충분한 봇이 연결되었습니다. 대화를 시작합니다!")
            else:
                print("⚠️  연결된 봇이 적지만 테스트를 계속 진행합니다.")
    
    def start_continuous_monitoring(self):
        """지속적 모니터링 시작"""
        print("\n💬 100개 봇이 지속적으로 대화를 시작합니다!")
        print("📊 30초마다 통계를 업데이트합니다...")
        print("💡 종료하려면 Ctrl+C를 눌러주세요\n")
        
        last_stats_time = time.time()
        last_detailed_stats = time.time()
        
        try:
            while self.test_running:
                time.sleep(5)  # 5초마다 체크
                
                if not self.test_running:
                    break
                
                # 30초마다 기본 통계
                if time.time() - last_stats_time >= 30:
                    self.print_current_stats()
                    last_stats_time = time.time()
                
                # 2분마다 상세 통계
                if time.time() - last_detailed_stats >= 120:
                    self.print_detailed_stats()
                    last_detailed_stats = time.time()
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Ctrl+C 감지됨. 100개 봇 대화를 종료합니다...")
            self.stop_test()
    
    def print_current_stats(self):
        """현재 통계 출력"""
        stats = self.manager.get_current_stats()
        elapsed = stats.get('elapsed_time', 0)
        
        print(f"\n📊 [{datetime.now().strftime('%H:%M:%S')}] 대화 상태 (경과: {elapsed/60:.1f}분)")
        print(f"🔗 연결된 봇: {stats['connected_bots']}/100")
        print(f"💬 총 대화: 전송 {stats['messages_sent']}, 수신 {stats['messages_received']}")
        
        if stats['latency']:
            print(f"⚡ 응답시간: {stats['latency']['avg']:.1f}ms")
        
        # 초당 메시지 처리량
        if elapsed > 0:
            msg_per_min = (stats['messages_sent'] / elapsed) * 60
            print(f"📈 대화량: {msg_per_min:.1f} 메시지/분")
        
        # 연결 상태 평가
        if stats['connected_bots'] >= 90:
            print("✅ 대화 상태: 매우 활발")
        elif stats['connected_bots'] >= 70:
            print("✅ 대화 상태: 활발")
        elif stats['connected_bots'] >= 50:
            print("⚠️  대화 상태: 보통")
        else:
            print("❌ 대화 상태: 저조")
        
        print("-" * 50)
    
    def print_detailed_stats(self):
        """상세 통계 출력"""
        stats = self.manager.get_current_stats()
        
        print(f"\n📈 상세 통계 - {datetime.now().strftime('%H:%M:%S')}")
        print("="*60)
        
        # 봇별 활동 상태 분석
        active_bots = 0
        total_messages = 0
        
        for bot_detail in stats.get('bot_details', []):
            if bot_detail['connected']:
                active_bots += 1
                total_messages += bot_detail['messages_sent']
        
        print(f"🤖 활성 봇: {active_bots}/100")
        print(f"💬 평균 메시지/봇: {total_messages/max(active_bots,1):.1f}")
        print(f"🌐 서버 부하: {stats['error_count']} 오류")
        
        if stats['latency']:
            lat = stats['latency']
            print(f"⚡ 응답시간 상세:")
            print(f"   평균: {lat['avg']:.1f}ms")
            print(f"   최소: {lat['min']}ms") 
            print(f"   최대: {lat['max']}ms")
        
        print("="*60)
    
    def stop_test(self):
        """테스트 중지"""
        if self.manager and self.test_running:
            print("\n🛑 100개 봇 대화를 중지합니다...")
            self.test_running = False
            self.manager.stop_test()
            print("✅ 모든 봇이 안전하게 종료되었습니다.")
            
            # 최종 통계 출력
            self.print_final_stats()
    
    def print_final_stats(self):
        """최종 통계 출력"""
        try:
            print("\n" + "="*80)
            print("📊 100개 봇 지속 대화 최종 결과")
            print("="*80)
            
            stats = self.manager.get_current_stats()
            
            print(f"⏱️  총 대화 시간: {stats['elapsed_time']/60:.1f}분")
            print(f"🤖 최대 동시 접속: {stats['connected_bots']}/100 봇")
            print(f"💬 총 대화량:")
            print(f"   전송: {stats['messages_sent']:,}개")
            print(f"   수신: {stats['messages_received']:,}개") 
            print(f"❌ 오류 수: {stats['error_count']}회")
            
            # 성과 분석
            if stats['elapsed_time'] > 0:
                msg_per_hour = (stats['messages_sent'] / stats['elapsed_time']) * 3600
                print(f"📈 시간당 대화량: {msg_per_hour:,.0f} 메시지")
                
                uptime_rate = (stats['connected_bots'] / 100) * 100
                print(f"📊 평균 가동률: {uptime_rate:.1f}%")
            
            if stats['latency']:
                print(f"⚡ 평균 응답시간: {stats['latency']['avg']:.1f}ms")
            
            # 통계 파일 저장
            filename = self.manager.export_stats()
            if filename:
                print(f"💾 대화 기록: '{filename}'")
            
            print("\n🎉 100개 봇 지속 대화 테스트 완료!")
            print("="*80)
            
        except Exception as e:
            print(f"최종 통계 출력 중 오류: {e}")
    
    def cleanup(self):
        """정리 작업"""
        if self.manager:
            try:
                self.manager.stop_test()
            except:
                pass


def main():
    """메인 함수"""
    print("🤖💬 100개 봇 지속 대화 테스트를 시작합니다!")
    print("💡 이 테스트는 100개 봇이 계속해서 대화하는 모드입니다.")
    print("⚠️  서버에 지속적인 부하가 가해집니다.")
    print()
    
    # 확인 메시지
    confirm = input("100개 봇 지속 대화를 시작하시겠습니까? (y/n): ")
    if confirm.lower() != 'y':
        print("테스트를 취소했습니다.")
        return
    
    # 서버 확인
    print("\n💡 서버가 실행 중인지 확인해주세요!")
    input("서버 준비가 완료되면 Enter를 눌러주세요...")
    
    # 테스트 실행
    test = Persistent100BotTest()
    
    try:
        test.start_persistent_chat()
    except Exception as e:
        print(f"❌ 예상치 못한 오류 발생: {e}")
    
    print("\n👋 100개 봇 지속 대화가 완전히 종료되었습니다!")


if __name__ == "__main__":
    main()
