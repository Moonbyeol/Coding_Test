def solution(letter):
    answer = []
    morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                   "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                   "..-","...-",".--","-..-","-.--","--.."]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    morse = {morse_codes[i]: alphabet[i] for i in range(len(alphabet))}
    for i in letter.split():
        answer.append(morse[i])
    return ''.join(answer)