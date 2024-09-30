# 동영상 재생기
def solution(video_len, pos, op_start, op_end, commands):
    op_start_min = int(op_start.split(":")[0])
    op_start_sec = int(op_start.split(":")[1])
    op_end_min = int(op_end.split(":")[0])
    op_end_sec = int(op_end.split(":")[1])
                
    new_min = int(pos.split(":")[0])
    new_sec = int(pos.split(":")[1])
    video_min = int(video_len.split(":")[0])
    video_sec = int(video_len.split(":")[1])
    
    # 오프닝 건너뛰기
    def opening(new_min,new_sec):
        if op_start_min < new_min < op_end_min:
            new_min = op_end_min
            new_sec = op_end_sec
        elif op_start_min == new_min:
            if op_start_min == op_end_min:
                if op_start_sec <= new_sec <= op_end_sec:
                    new_min = op_end_min
                    new_sec = op_end_sec
            else:
                if op_start_sec <= new_sec:
                    new_min = op_end_min
                    new_sec = op_end_sec
        elif new_min == op_end_min:
            if new_sec <= op_end_sec:
                new_min = op_end_min
                new_sec = op_end_sec
        return new_min,new_sec
    
    for i in commands:
        new_min, new_sec = opening(new_min,new_sec)
        # 10 초 뒤로
        if i == "prev":
            new_sec -= 10
            if new_sec < 0 :
                new_min -=1
                new_sec += 60
                if new_min < 0:
                    new_min = 0
                    new_sec = 0
        # 10 초 앞으로 
        elif i == "next":
            new_sec += 10
            if new_sec >= 60:
                new_min +=1
                new_sec -=60
            if new_min > video_min:
                new_min = video_min
                new_sec = video_sec
            elif new_min == video_min:
                if new_sec >= video_sec:
                    new_min = video_min
                    new_sec = video_sec
                        
    new_min, new_sec = opening(new_min,new_sec)
    new_min = str(new_min)
    new_sec = str(new_sec)
    if len(new_min) == 1:
        new_min = "0"+str(new_min)
    if len(new_sec) == 1:
        new_sec = "0"+str(new_sec)
    result = new_min + ":"+new_sec
    return result
            