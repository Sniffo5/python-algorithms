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

---
### DAG 3 | 08-12-2025
Idag så fixade jag så att jag min "test" så att jag kör igenom alla sortering algoritmer 3 gånger per typ av genereringstyp och sedan tar medelvärdet och skriver ut allt snyggt i en tabell. Det tog så lång tid eftersom jag skulle fixa så det var enkelt att lägga till fler algoritmer och genertaionstyper. Jag gjorde så de flesta delarna av testen och utskriften var dynamiska. Jag fixade även min selection sort då jag märkte jag hade glömt -i i en av looparna.

---
---


||Random| Few Unique | Semi Sorted | Sorted Reverse |
|------------|------|------------|-------------|----------------|
|**Bubble Sort**|5040.4 ms|4518.5 ms|2922.9 ms|6371.2 ms|
|**Selection Sort**|2405.2 ms|2303.7 ms|1917.2 ms|2154.8 ms|
|**Insertion Sort**|2204.4 ms|1980.5 ms|46.8 ms|4146.8 ms|
|**Python Sort**|1.2 ms|0.9 ms|0.4 ms|0.1 ms|

*10000 tal, 100 unika tal, 100 slumpmässiga tal, tal mellan 1 och 20000000*

# Analys
### 1. Vilken alogritm var snabbast i de olika fallen?

För helt slumpmässiga tal så var insertion sort snabbast, för endast några unika tal så var insertion sort också snabbast, för sorterad data med några felplacerade tal så var insertion sort snabbast med stort marginal, för data som är omvänt så är selection sort snabbast.

### 2. Varför fungerar Insertion Sort bra på nästan sorterad data?

Insertion sort fungerar bra på nästan sorterad data då algoritmen hittar rätt position för varje osorterat element. Ifall listan är nästan helt sorterad så skippar den allt fram till där den är osorterad och sedan stoppar det osorterade talet i rätt position. På så sätt minskas onödiga förflyttnigar av tal då den enbart tar de som är i fel position och stoppar dem rätt. Till skillnad från t.ex. en bubble sort som flyttar alla tal oavsett om de är i ordning eller inte.

### 3. Varför ändras inte tiden för Selection Sort så mycket beroende på datan?

Selection sort kommer ta ungefär lika lång tid oavsett hur datan ser ut. Det är på grund av att algoritmen går ut på att en för en bygga upp listan genom att hitta nästa tal. Den går genom alla tal hittar den som är näst på tur och stoppar den i slutet av den nuvarande sorterade delen. Algoritmen gör alltid samma antal jämföresler oavsett hur datan ser ut. Det är bara olika många byten som sker som ger lite skillnad i tiden, men då den jämför samma antal gånger alltid så blir tiden väldigt lik.

### 4. Vilket fall var svårast för Bubble Sort?

Bubble Sort hade svårast med att talen var i rätt ordning men omvända. Det är då det behövde skicka talen så långt som möjligt varje gång. Bubble sort går ut på att talen ska "flyta upp" till rätt position. Så när talen är i omvänd ordning så är talen lägre närmare slutet. Då måste de transporteras en väldigt lång sträcka till början av listan.

