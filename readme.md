# Loggbok

### DAG 1 | 01-12-2025

Jag började skapa de olika sökalgoritmerna. Gjorde klart bubble-sort men fastnade på selection-sort. Fick selection-sort nästan att fungera, den sorterar till [8, 0, 1, 2, 3, 4, 5, 6, 7, 9] vilket är nästan rätt. 

Näst gång ska jag fixa selection-sort så att den fungerar samt göra insertion-sort

---
### DAG 2 | 05-12-2025

Jag började med att försöka felsöka selection-sort och råkade börja konvertera den till en insertion sort så jag stoppade in den isnertion-metoden. När jag försökte felsöka metoden så kunde jag för mitt liv inte förstår hur den kunde sortera på det sättet den gjorde, då kom jag till slut fram till att jag inte kopierade den osorterade datan på riktigt utan bara skapade en ny variabel som ändå reffereade till ursprungs listan. När jag väl kunde använda rätt data så blev det mycket enklare att koda metoden rätt. Jag hamnade dock i ännu ett sidospår med min for loopen 
```python 
for j in range(i-1, -1, -1):
```
Jag hade urspruligen i mitten en nolla istället för -1 och då körde loopen helt genom. Efter det var löst så fungerade metoden ändå för sitt liv inte, efter att ha ritat upp listan på papper och manuellt gått genom varje itteration av loopen kunde jag tillslut hitta att felet var hur jag tilldelade värdet efter att jag hade flyttat alla element som var större åt höger. Problemet var att istället för att tilldela den position längst till vänster som var nu ledig tilldelade jag värdet till den position som jämförelsetalet hade ursprungat från. Men det kunde som tur är lösas enkelt. 

Efte att jag hade gjort klart min insertion-sort så gjorde jag även en selection-sort snabbt, och på så sätt vara klar med de tre första algoritmerna.

Jag gjorde sen ett Gen class och gjorde den första metod som generar en lista me slumpässiga tal beroende på olika paramterar användaren matar in.

Jag testade sedan alla 3 algorithmer på 100 tal och alla fungerade.