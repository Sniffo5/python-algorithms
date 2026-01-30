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
Idag så fixade jag så att jag min "test" så att jag kör igenom alla sortering algoritmer 3 gånger per typ av genereringstyp och sedan tar medelvärdet och skriver ut allt snyggt i en tabell. Det tog så lång tid eftersom jag skulle fixa så det var enkelt att lägga till fler algoritmer och genertaionstyper. Jag gjorde så de flesta delarna av testen och utskriften var dynamiska. Jag fixade även min selection sort då jag märkte jag hade glömt -i i en av looparna samt använda min_index i jämförelserna istället för j. näst på tur blir att skriva analysen sedan göra merge sort efteråt ifall jag har mer tid.

---
### DAG 4 | 11-01-2025
Idag skrev jag klart min analys och gjorde min merge-sort. Merge-sort var riktigt klurigt. Det var inte svårt att första hur det fungerade men det var svårt att implementera det. Jag hade många problem där med bland annat att repptera funktionerna tillräckligt många gåner samt att lägga till talen i slutet rätt efter jag har sorterat men ändå har tal kvar. jag körde även for loopar med if statser inuti men bytte ut det til while loppar för att förenkla koden men samt får den att fungera i alla situationer. Det var väldigt spänande att få ta sig ann en soppas svår alogirtm och det tog många timmar av att jklura för att få den att fungera.

---
---

# Analys

||Random| Few Unique | Semi Sorted | Sorted Reverse |
|-|-|-|-|--|
|**Bubble Sort**|2315.9 ms|2106.3 ms|1224.1 ms|2869.5 ms|
|**Selection Sort**|1013.0 ms|1000.3 ms|851.6 ms|938.5 ms|
|**Insertion Sort**|1002.8 ms|968.7 ms|13.4 ms|1897.0 ms|
|**Python Sort**| 0.7 ms|0.5 ms|0.2 ms|0.04 ms|

***10000 tal, 100 unika tal, 100 slumpmässiga tal, tal mellan 1 och 20000000***\
***CPU:** 9800x3d, **RAM:** 16 GB 6000 MHZ CL30 DDR5*

---

## 1. Vilken alogritm var snabbast i de olika fallen?

För helt slumpmässiga tal så var **insertion** sort snabbast (**1003 ms**), för endast några unika tal så var **insertion** sort också snabbast (**969 ms**), för sorterad data med några felplacerade tal så var **insertion** sort snabbast med stor marginal (**13.4 ms**), för omvänd ordning så var **selection** sort snabbast (**939 ms**). För omvänd data så är Insertion Sort så signifikant slöare så det ser ut som att det är något fel med algoritmen då den är ungefär dubbelt så slö som när den kör på andra data typer.

## 2. Varför fungerar Insertion Sort bra på nästan sorterad data?

Insertion sort fungerar bra på nästan sorterad data då algoritmen hittar rätt position för varje osorterat element. Ifall listan är nästan helt sorterad så skippar den allt fram till där den är osorterad och sedan stoppar det osorterade talet i rätt position. På så sätt minskas onödiga förflyttnigar av tal då den enbart tar de som är i fel position och stoppar dem rätt. Till skillnad från t.ex. en bubble sort som flyttar alla tal oavsett om de är i ordning eller inte.

## 3. Varför ändras inte tiden för Selection Sort så mycket beroende på datan?

Selection sort kommer ta ungefär lika lång tid oavsett hur datan ser ut. Det är på grund av att algoritmen går ut på att en för en bygga upp listan genom att hitta nästa tal. Den går genom alla tal hittar den som är näst på tur och stoppar den i slutet av den nuvarande sorterade delen. Algoritmen gör alltid samma antal jämföresler oavsett hur datan ser ut. Det är bara olika många byten som sker som ger lite skillnad i tiden, men då den jämför samma antal gånger alltid så blir tiden väldigt lik.

## 4. Vilket fall var svårast för Bubble Sort?

Bubble Sort hade svårast med att talen var i rätt ordning men omvända. Det är då det behövde skicka talen så långt som möjligt varje gång. Bubble sort går ut på att talen ska "flyta upp" till rätt position. Så när talen är i omvänd ordning så är talen lägre närmare slutet. Då måste de transporteras en väldigt lång sträcka till början av listan.

## 5. Hur ökar körtiden när du fördublar listans storlek?

||Random| Few Unique | Semi Sorted | Sorted Reverse |
|-|-|-|-|--|
|**Bubble Sort**|8826.9 ms|8106.3 ms|4741.98 ms|11008.9 ms|
|**Selection Sort**|3947.5 ms|3915.0 ms|3413.4 ms|3645.5 ms|
|**Insertion Sort**|3823 ms|3562.2 ms|26.1 ms|7314.8 ms|
|**Python Sort**| 1.6 ms|1.1 ms|0.15 ms|0.08 ms|

***20000 tal, 100 unika tal, 100 slumpmässiga tal, tal mellan 1 och 20000000***\
***CPU:** 9800x3d, **RAM:** 16 GB 6000 MHZ CL30 DDR5*

När jag dubblar antalet tal som sorteras så ökas tiden i snitt lite under 4 gånger. **Bubble Sort** på helt slumpmässiga tal går från **2316 ms** till **8827 ms** (×3,8), några få unika går från **2106 ms** till **8106 ms** (×3,85), semi-sorterade går från **1224.1 ms** till **4741.98 ms** (×3,88), och omvänd sortering från **2869.5 ms** till **11008.9 ms** (×3,83).

**Selection Sort** går från **1013.0 ms** till **3947.5 ms** (×3,88) för helt slumpmässiga tal, från **1000.3 ms** till **3915.0 ms** (×3,91) för några få unika, semi-sorterade från **851.6 ms** till **3413.4 ms** (×4,01), och omvänd sortering från **938.5 ms** till **3645.5 ms** (×3,88).

**Insertion Sort** ökar från **1002.8 ms** till **3823 ms** (×3,81) för helt slumpmässiga tal, från **968.7 ms** till **3562.2 ms** (×3,68) för några få unika, semi-sorterade från **13.4 ms** till **26.1 ms** (×1,94), och omvänd sortering från **1897.0 ms** till **7314.8 ms** (×3,86).

**Python Sort** går från **0.7 ms** till **1.6 ms** (×2,29) för helt slumpmässiga tal, från **0.5 ms** till **1.1 ms** (×2,20) för några få unika, semi-sorterade från **0.2 ms** till **0.15 ms** (×0,75), och omvänd sortering från **0.04 ms** till **0.08 ms** (×2,00).

I snitt blir förändringsfaktorn för **Bubble Sort**, **Selection Sort** och **Insertion Sort** runt 3,85 med undantag för **Insertion Sort** på **semi-sorterade** tal som låg på **×1,94** vilket var mer likt förändrignsfaktorn för pythons inbyggda sorteringsalgoritm som i snitt låg på **×1,81**.

Jag körde sedan tester på **30000** , **40000** och **50000** element. **30000** var i snitt lite under **×9** föruotm insertion som låg närmare **×7,5**, **40000** var i snitt lite under **×16** förutom Insertion som låg närmare **×13**, **50000** var i snitt lite under **×25**

Det syns då ett väldigt tydligt mönster mellan antal element och förändringsfaktorn på tiderna. När vi dubblade element så blev tiden kvadrerad, när vi tripplade antal element så nio-dubblades tiden, när vi fyr-dubblade antal element så blev tiden sextondubblat och till slut när vi femdubblade elementen så lev tiden tjugiofem gånger mer än från början. Tiden det tar för att sortera elementen följer alltså ett mönster av att den ökningen vi gör på elementen kvadreras för att få förändringsfaktorn.\
Alla tre av de sorteringsalgoritmerna jag gjorde har samma algoritmisk komplexitet på ***O*(n^2)**. Det betyder att antal steg för att sortera listan är n^2 då *O* blir överflödig när vi når högre n. På grund av den kvadratiska komplexiteten hos dessa algoritmer så blir då tiden den tar kvadrerad. Jämfört med pythons inbyggda sorteringsalgoritm som inte har en komplexitet på n^2 så blir inte förändringsfaktorn där lika stor **(×2 => ×1.81 , ×3 => ×3.5, ×4 => ×4.6, ×5 => ×6.04 )**. Istället är den mycket mer lik förändringen på antal element då den inte har en lika stor tidskomplexitet.

## 6. Hur mycket snabbare är Pythons inbyggda sorteringsalgoritm för listor? Hur funkar den egentligen? 

Pythons inbyggda sorteringslgoritm är mycket snabbare. För mitt orginella test på 10000 element så var den mellan 67 till 71725 gånger snabbare än de jag själv kodade. Jämfört med bubble sort på en omvänd lista så är den signifikant snabbare **0.04 ms** kontra **2870 ms**. Det är på grund av hur den är uppbyggd, pythons egna sorteringsalgoritm kör timesort som kör en blanding av olika algoritmer. Den letar först upp redan delvis sorterade sekvenser i listan och kör insertion sort på dem delarna och sedan kör den merge sort på alltihop. På så sätt lyckas algoritmen får en betydligt mindre komplexitet som i värsta fall bara blir *O*(n log n).


# Frågor om merge sort

## 1. Är Merge Sort snabbare än dina andra algoritmer? 

||Random| Few Unique | Semi Sorted | Sorted Reverse |
|-|-|-|-|--|
|**Bubble Sort**|2214.3 ms|2027.2 ms| 1170.9 ms|2690.3 ms|
|**Selection Sort**|1002.2 ms| 988.7 ms|832.2 ms|914.8 ms|
|**Insertion Sort**|943.9 ms|918.8 ms|12.5 ms|1811.8 ms|
|**Merge Sort**|9.6 ms|9.45 ms|8.3 ms| 7.75 ms|
|**Python Sort**| 0.68 ms| 0.54 ms|0.069 ms| 0.03 ms|

***10000 tal, 100 unika tal, 100 slumpmässiga tal, tal mellan 1 och 20000000***\
***CPU:** 9800x3d, **RAM:** 16 GB 6000 MHZ CL30 DDR5*

Merge sort är snabbbare i alla fall, dock har jag i andra tester regelbundet fått att Insertion Sort är snabbare på semi sorted data, vilket hade förklarat varför python sort delvis anvdänder sig gav insertion sort. Dock är Pythons inbyggda fortfarande milsvis snabbare, det är då på grund av att den anpassar algoritm-användningen för datan och på så sätt lyckas sortera datan betydligt snabbare.


## 2. Varför kräver Merge Sort extra minne? 

Merge sort kräver extra minne då den hela tiden skapar nya listor medans en algoritm som bubble sort inte gör det utan använder samma lista hela vägen genom.