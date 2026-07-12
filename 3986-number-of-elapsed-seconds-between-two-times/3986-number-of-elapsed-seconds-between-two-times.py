class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        len(startTime)==8
        len(endTime)==8
        hh, mm, ss = map(int, startTime.split(":"))
        startSeconds = (hh * 3600) + (mm * 60) + ss
        hh, mm, ss = map(int, endTime.split(":"))
        endSeconds = (hh * 3600) + (mm * 60) + ss
        difference = endSeconds - startSeconds
        if difference < 0:
            difference += 86400
        return difference
    
        