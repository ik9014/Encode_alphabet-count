import operator

# 파일 경로 설정
file_input_original = "C:/Computer Network/alphabet.txt" # 원본 파일
file_output_count = "C:/Computer Network/Key.txt" # 알파벳 빈도 수 (오름차순)
file_input_count = "C:/Computer Network/Key.txt" # 키 파일 (암호화에 사용)
file_output_encode = "C:/Computer Network/Encode.txt" #암호화된 데이터
file_output_decode = "C:/Computer Network/Decode.txt" #복호화된 데이터


# 알파벳 빈도수를 저장할 딕셔너리 초기화
count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0,
         'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
         'k':0, 'l':0, 'm':0, 'n':0, 'o':0,
         'p':0, 'q':0, 'r':0, 's':0, 't':0,
         'u':0, 'v':0, 'w':0, 'x':0, 'y':0,
         'z':0}


# 빈도수를 정렬하여 저장할 딕셔너리
sorted_count = {}

# 함수 기능: 알파벳 빈도수를 계산한다
# 입력: X (없음)
# 출력: X (없음)
def count_alphabet():
    try:
        # 원본 파일을 읽기 모드로 연다
        with open(file_input_original, "r") as fin:
            while True:
                data = fin.read(1) # 파일에서 한 글자씩 읽는다
                
                if not data: # 파일 끝 도달시 반복 종료
                    break
                
                # 알파벳 감지시 해당 알파벳 빈도수 증가
                if 'A' <= data <= 'Z':
                    count[data.lower()] += 1           
                elif 'a' <= data <= 'z':
                    count[data] += 1
        
        # 빈도수를 기준으로 오름차순으로 정렬   
        sorted_count = sorted(count.items(), key=operator.itemgetter(1))
        
        # 결과를 파일에 저장한다
        with open(file_output_count, "w") as fout:
            for dic_key, dic_value in sorted_count:
                fout.write(f"{dic_key} = {dic_value}\n")
        
        print ("[키값 생성 완료]\n파일경로 :",file_output_count, "\n")
        
    # 예외 처리
    except FileNotFoundError:
        print(f"\n!!!파일을 찾을 수 없습니다!!!: {file_input_original}")
    except Exception as e:  
        print(f"\n!!!예기치 않은 오류가 발생했습니다!!!: {e}")
        
        
# 함수 기능: 알파벳 빈도에 따라 데이터를 암호화한다
# 입력: X (없음)
# 출력: X (없음)
def encode():
    try:
        # 암호화 결과를 저장할 파일 생성
        with open(file_output_encode, "w") as encode:
            while True:
                break
        
        # 키 파일을 읽어 알파벳과 빈도수는 sorted_count에 저장
        with open(file_input_count, "r") as fin_count:
            while True:
                line=fin_count.readline()
                if not line: # 파일 끝 도달시 반복 종료
                    break
                
                key, value = line.split(' = ')
                sorted_count[key] = int(value)
        
        # count, sorted_count 딕셔너리를 리스트로 변환
        count_list = list(count.items())
        sorted_count_list = list(sorted_count.items())
        
        # 원본 파일을 읽어 암호화 진행
        with open(file_input_original, "r") as fin_original:
            with open(file_output_encode, "a") as fout_encode:
                while True:
                    data = fin_original.read(1)
                    if not data:
                        break
                    
                    # 알파벳이면 암호화, 그 외의 문자는 그대로 복사
                    if 'A' <= data <= 'Z' or 'a' <= data <= 'z':
                        data = data.lower()
                        
                        for dic_key, dic_value in count_list:
                            if data == dic_key:
                                index = count_list.index((dic_key, dic_value))
                                data_encoded = sorted_count_list[index][0] #암호화된 알파벳

                                fout_encode.write(data_encoded)
                    else:
                        fout_encode.write(data)
                                        
        print("[암호화 완료]\n파일경로: ",file_output_encode, "\n")      
        
    # 예외 처리                 
    except FileNotFoundError as e:
        print(f"\n!!!파일을 찾을 수 없습니다!!!: {e}")
    except Exception as e:
        print(f"\n!!!암호화 중 오류가 발생했습니다!!!: {e}")


# 함수 기능: 암호화된 데이터를 복호화한다
# 입력: X (없음)
# 출력: X (없음)           
def decode():
    try:
        # 복호화 결과를 저장할 파일 생성
        with open(file_output_decode, "w") as decode:
            while True:
                break   
            
        # count, sorted_count 딕셔너리를 리스트로 변환
        count_list = list(count.items())
        sorted_count_list = list(sorted_count.items())
        
        # 암호화된 파일을 읽어 복호화 진행
        with open(file_output_encode, "r") as fin_encode:
            with open(file_output_decode, "a") as fout_decode:
                while True:
                    data = fin_encode.read(1)
                    if not data:
                        break
                    
                     # 알파벳이면 복호화, 그 외의 문자는 그대로 복사
                    if 'A' <= data <= 'Z' or 'a' <= data <= 'z':
                        data = data.lower()
                        
                        for dic_key, dic_value in count_list:
                            if data == dic_key:
                                index = sorted_count_list.index((dic_key, dic_value))
                                data_encoded = count_list[index][0] #복호화된 알파벳
                                                               
                                fout_decode.write(data_encoded)
                    else:
                        fout_decode.write(data)
                        
        print("[복호화 완료]\n파일경로: ",file_output_decode, "\n")    
        
    # 예외 처리             
    except FileNotFoundError as e:
        print(f"\n!!!파일을 찾을 수 없습니다!!!: {e}")
    except Exception as e:
        print(f"\n!!!복호화 중 오류가 발생했습니다!!!: {e}")


count_alphabet() # 키값 생성
encode() # 암호화
decode() # 복호화
