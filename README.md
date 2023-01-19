
# CarDashboard

CarDashboard to symulator kokpitu samochodu napisany w języku Python z użyciem biblioteki Pygame. Program pozwala na symulację różnych elementów kokpitu, takich jak prędkościomierz, obrotomierz, kontrolki ostrzegawcze, kierunkowskazy oraz klakson.

## Sterowanie:
- Guzik Start/Stop - odpowiada za wyłączenie i włączenie silnika 
- Strzałka w prawo - włączenie kierunkowskazu w prawo
- Strzałka w lewo - włączenie kierunkowsku w lewo
- Spacja - włączenie klaksonu
- Program symuluje również losowanie błędów w kokpicie, które są wyświetlane jako kontrolki ostrzegawcze.
- Zwiększenie obrotów i prędkościomierza jest sterowane pedałem gazu

Dodatkowo, program posiada funkcję debugowania, którą można włączyć w pliku CarDashboard.py ustawiając zmienną debug na True. Po włączeniu tej funkcji, program będzie drukował informacje o wciśniętych przyciskach na konsoli.

Uwaga: Program jest tylko symulatorem i nie jest przeznaczony do użytku w rzeczywistych pojazdach.


## FAQ
#### Opis funkcji i zmiennych:

`turnOnAllIcons()`: ta funkcja zwraca tuple z 9 wartościami True, co oznacza, że wszystkie kontrolki ostrzegawcze są włączone.

`turnOffAllIcons()`: ta funkcja zwraca tuple z 9 wartościami False, co oznacza, że wszystkie kontrolki ostrzegawcze są wyłączone.

`blitRotate(surf, image, pos, angle=0)`: ta funkcja jest odpowiedzialna za obrót obrazu przy jego wyświetlaniu na ekranie. Przyjmuje ona następujące argumenty:

- `surf` - powierzchnia na której ma być wyświetlony obraz
- `image` - obraz, który ma być wyświetlony
- `pos` - pozycja, na której ma być wyświetlony obraz
- `angle` - kąt obrotu obrazu (domyślnie 0)

`rot_center(image, angle`): ta funkcja jest odpowiedzialna za obrót obrazu przy zachowaniu jego pozycji i rozmiaru. Przyjmuje ona dwa argumenty:

- `image` - obraz, który ma być obrócony
- `angle` - kąt obrotu obrazu

`dispalyPosition(positionInPrecent=(0, 0))`: ta funkcja jest odpowiedzialna za przeliczanie procentowej pozycji na pozycję w pikselach na ekranie. Przyjmuje ona jeden argument - pozycję w procentach i zwraca pozycję w pikselach

`debug` : jest to zmienna globalna, która umożliwia włączenie/wyłączenie debugowania. Po włączeniu debugowanie, program drukuje na konsoli informacje o wciśniętych przyciskach.

`abs`, `checkEngine`, `esp`, `lights`, `oil`, `reserve`, `temp`, `traction`, `warning`, `kierunkowskaz_prawy`, `kierunkowskaz_lewy`: te zmienne przechowują obrazy odpowiadające kontrolkom ostrzegawczym lub kierunkowskazom.

`carParameters`: jest to obiekt klasy Vehicle , który jest używany do przechowywania parametrów pojazdu, takich jak prędkość, RPM, czy stan kierunkowskazów. Klasa ta posiada metody getter i setter dla tych parametrów, co pozwala na łatwe uzyskanie lub zmianę tych wartości.

`pygame.mixer.init()`: ta linijka kodu jest odpowiedzialna za inicjalizację modułu dźwięku w Pygame.

`screen = pygame.display.set_mode((displaySizeWidth, displaySizeHeight))`: ta linijka kodu jest odpowiedzialna za utworzenie okna o określonych rozmiarach.

`pygame.display.set_caption('CarDashboard')`: ta linijka kodu jest odpowiedzialna za ustawienie tytułu okna.

`clock = pygame.time.Clock()`: ta linijka kodu tworzy zegar, który jest używany do kontrolowania płynności animacji.

`for event in pygame.event.get():`: ta pętla jest odpowiedzialna za pobieranie wszystkich zdarzeń (np. naciśnięcia przycisków na klawiaturze) i przetwarzanie ich.

`if event.key == pygame.K_RIGHT:`: ta instrukcja jest odpowiedzialna za sprawdzenie czy wciśnięto strzałkę w prawo i włączenie odpowiednio kierunkowskazu w prawo.

`if event.key == pygame.K_LEFT:`: ta instrukcja jest odpowiedzialna za sprawdzenie czy wciśnięto strzałkę w lewo i włączenie odpowiednio kierunkowskazu w lewo.

`if event.key == pygame.K_SPACE:`: ta instrukcja jest odpowiedzialna za sprawdzenie czy wciśnięto spację i włączenie dźwięku klaksonu.

`if event.type == pygame.QUIT:`: ta instrukcja jest odpowiedzialna za sprawdzenie czy zdarzenie to jest zamknięciem okna

`pygame.display.update()`: ta linijka kodu jest odpowiedzialna za wyświetlenie wszystkich zmian na ekranie.

`clock.tick(60)`: ta linijka kodu jest odpowiedzialna za ustawienie liczby klatek na sekundę, co pozwala na płynną animację.

`pygame.quit()`: ta linijka kodu jest odpowiedzialna za zamknięcie modułu Pygame po zakończeniu działania programu.

#### Uruchomienie programu:

Aby uruchomić program należy mieć zainstalowany Python oraz bibliotekę Pygame. Następnie należy pobrać plik CarDashboard.py i uruchomić go przy pomocy polecenia python CarDashboard.py w konsoli.




## Instalacja wymaganych bibliotek

By program działa prawidłowo wymagane jest zainstalowanie załączonych w kodzie bibliotek.



```bash
  pip install pygame

  pip install time
```
    
#### Wymagane jest posiadanie ekranu o rozdizelczości Full HD (1920 x 1080 px)!!!
