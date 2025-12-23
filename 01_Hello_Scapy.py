# scapy
# 파이썬 기반 강력한 패킷 조작 라이브라러 (패킷 스니퍼/분석도구)
# 네트워크 패킷을 캡쳐, 생성, 수정, 전송, 분석할 수 있음

# 본 프로젝트의 주제
# 패킷 스니핑 + 필터링 (및 로그 분석) 구현
# 1. 네트워크에 흐르는 패킷을 실시간으로 캡쳐
# 2. 조건(특정 ip, 특정 포트, 특정 프로토콜)에 따라 필터링
# 3. 로그 분석 (추가 점수)

from scapy .all import sniff

# 패킷 5개 캡쳐 후 출력
sniff(count=5, prn=lambda x:print(x))
# 특정 프로토콜(tcp)만 캡쳐
sniff(filter="tcp", prn=lambda x:print(x))

# 특정 프로토콜의 패킷 5개 캡쳐 후 출력
sniff(filter="tcp", count=5, prn=lambda x:print(x))


from scapy.all import IP, ICMP, send

# ICMP 패킷 하나 생성
packet = IP(dst ='8.8.8.8') / ICMP()
for _ in range(1):
    send(packet)

# 패킷 구조 확인
packet.show()