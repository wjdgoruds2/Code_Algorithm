class ThailandPackage:
    def detail(self):
        print("[ 태국 패키지 3박 5일 ] 방콕, 파타야 야행 (야시장 투어) 50만원")





#########모듈 직접 실행
if __name__=="__main__":
    print("Thailand 모듈을 직접 실행")
    print("직접 실행 시 실행된다.")
    trip_to=ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출")