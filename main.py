from os import system, name
import time

def clear():
  if name == 'nt':
    system('cls')
  else:
    system('clear')

def displayQuest(quest):
  clear()
  print()
  for sentence in quest:
    print(sentence)
  print()

def nextQuest(quest, nextQ):
  displayQuest(quest)
  input("(ENTER)>")
  nextQ()

def selectDecision(quest, options):
  displayQuest(quest)
  for i, option in enumerate(options):
    print(f"{i+1}. {option[0]}")
  print()

  def getAnswer():
    try:
      answer = int(input(">"))
      if answer >=1 and answer <= len(options):
        return answer
      else:
        return False
    except ValueError:
      return False

  answer = getAnswer()
  if not answer:
    while True:
      print()
      print(f"Podaj liczbê (od 1 do {len(options)}):")
      answer = getAnswer()
      if answer:
        break

  options[answer-1][1]()

def boolDecision(quest, ifTrue = False, ifFalse = False):
  displayQuest(quest)

  answer = input("(T/N)>").lower()
  if answer == "t" and ifTrue:
    ifTrue()
  elif ifFalse:
    ifFalse()

def textAnswer(quest, answerVal, ifValid, ifNotValid):
  displayQuest(quest)

  answer = input(">").lower()
  if answerVal(answer) and ifValid:
    ifValid()
  elif ifNotValid:
    ifNotValid()

def test(questions):
  results = []
  for question in questions:
    displayQuest(question[0])
    answer = input(">")
    results.append(question[1](answer))
  score = results.count(True)
  return score


def praktyka():
  def praktyka1A():
    def praktykaTest():
      score = test([
        [
          [
            "Wyświetl wszystkie grupy (w cmd):"
          ],
          lambda answer : answer == "net localgroup"
        ], [
          [
            "Jedną komendą utwórz foldery 1,2,dupa,4,5,6,cosseksownego,8,9,10"
          ],
          lambda answer : answer == "mkdir 1,2,dupa,4,5,6,cosseksownego,8,9,10"
        ], [
          [
            "Jaką komendą w diskparcie zrobisz partycje podstawową o wielkości 16BG?"
          ],
          lambda answer : answer == "create partition primary size=16384"
        ], [
          [
            "Zakładając że graficznie jest włączona,",
            "ustaw quotę na dysku z: o progu maksymalnym 2gb, ostrzeżenia 1,8gb dla użytkownika dupeczka_1",
            "(PRZLICZAJĄC ROZMIARY ZAOKRĄGL W GÓRĘ)"
          ],
          lambda answer : answer == "fsutil quota modify z: 1887437 2097152 dupeczka_1"
        ], [
          [
            "Utwórz użytkownika Jan Kowalski (pracownik1) z hasłem 1qazxsW@ poprawnie"
          ],
          lambda answer : answer == r'net user "kowalskijan" "1qazxsW@" /fullname:"Jan Kowalski" /comment:"pracownik1" /active:yes /logonpasswordchg:yes /add'
        ], [
          [
            "Na dysku X:\ znajduje się folder Dane. Ustaw pełne prawa użytkownikowi dupeczka_1"
          ],
          lambda answer : answer == "icacls x:\Dane /inheritance:R /grant dupeczka_1:F /t"
        ], [
          [
            "Na dysku X:\ znajduje się folder Dane. Ustaw prawa administorom pełne prawa, a grupie użytkownicy odczyt i zapis"
          ],
          lambda answer : answer == "icacls x:\Dane /inheritance:R /grant Administratorzy:F użytkownicy:rw /t"
        ]
      ])
      print()
      print('Wynik: ', f"{score}/7")

    nextQuest([
      "No to puszczją dupochrony, wyciągają karteczki i piszą pytania!"
    ], praktykaTest)

  def praktyka1B():
    nextQuest([
      "Debilizm!! Dupę chroni!!"
    ], praktyka1A)

  def answerVal(answer):
    return answer == "chroni dupe" or answer == "chroni dupê"

  textAnswer([
    "Kliś rozpoczął lekcję. Zadaje pytanie: co robi dupochron?"
  ], answerVal, praktyka1A, praktyka1B)


def kufajka():
  def poscig():
    print("poscig")
    # MINIGRA JAKAŚ JAK UCIEKNIESZ TO NIE TRAFIASZ NA PRAKTYKE MUSISZ NA DZIEN MIŁOSIEDZIA

  def kufajka1A():
    def kufajka2A():
      nextQuest([
        "Zanosisz ocieplające narzędzie zła na tej ziemii do magicznego grobowca zwanego szatnią.",
        "",
        "Dostajesz talizman zwany przepustką,",
        "który pozwoli ci wejść do magicznej sali 51.",
        "Po przyjściu pod tą salę widzisz profesora sprawdzającego przepustki i filcoki.",
        "Na całe szczęście odniosłeś kurtkę do szatni,",
        "a sezon na zostawianie butów się jeszcze nie zaczął.",
        "",
        "Na luzaku wbijasz do sali w porę na praktykę."
      ], praktyka)

    def kufajka2B():
      def kufajka3B():
        nextQuest([
          "W życiu podjąłeś wiele decyzji.",
          "Niektóre lepsze, niektóre gorsze.",
          "Ale to przebiło wszystko.",
          "",
          "Próbowałeś zignorować Klisia, ale Klisia się nie ingoruje.",
          "Ruszył za tobą w pościg. Nie daruje Ci tej zniewagi.",
          "Uciekasz przed profesorem po terenie całej szkoły,",
          "zaskakuje cię jego kondycja. Nigdy byś nie pomyślał,",
          "że będzie w stanie siedzieć ci non stop na ogonie.",
          "",
          "Odczuwasz już zmęczenie, aż tu nagle olśniło cię.",
          "Jedyna szansa. Pobiegnij na palarnie, wtop się w tłum.",
          "To jest jedyne co może cię teraz uratować.",
          "",
          "Prześlizgnij się między tłumem."
        ], poscig)

      selectDecision([
        "Niestety, nie pykło.",
        "",
        "Kliś stał na wejściu do sali i nawet nie miałeś szansy wejść do środka.",
        "Profesor zatrzymał cię w progu i złapał za kaptur od kufajki.",
        "\"Gdzie z tymi kurtkami?!\" - Głoś Klisia brzęczy ci w uchu.",
        "A może to ślina która wymskneła się do twojego ucha.",
        "",
        "W każdym razie przekaz jest prosty, musisz odnieść kufaję do szatni."
      ], [
        ["Odnoszę, wolę nie ryzykować. Raz już wpadłem, drugiego razu nie będzie.", kufajka2A],
        ["Jak już mówiłem, na przypale albo wcale. Mam na to papiery.", kufajka3B]
      ])

    selectDecision([
      "Bierzesz kufajkę, i wychodzisz na tą polską syberię.",
      "",
      "Piździ, ale nie jest ci aż tak zimno, w końcu po coś ją brałeś.",
      "Wbijasz do budynku szkoły, jest godzina 7:59.",
      "Niemalże spóźniony, nie chcesz dostać spóźnienia,",
      "bo przez ten jeden punkt spadnie ci zachowanie.",
      "Natomiast jeżeli weźmiesz kufajkę do sali to przypał będzie większy.",
      "",
      "Zanosisz kufajkę do szatni czy ryzykujesz?"
    ], [
      ["Odnoszę. Nie ma nic gorszego od gniewu profesora.", kufajka2A],
      ["Na przypale albo wcale.", kufajka2B]
    ])

  def kufajka1B():
    nextQuest([
      "Postanowiłeś nie brać kufajki, w końcu zdarzało się",
      "chodzić ze śmieciami w krótkich spodenkach w temperaturze 0 stopni.",
      "",
      "Nie masz kufajki, więc naturalnie nie musisz zanosić jej do szatni.",
      "Listopad listopadem, śnieg jeszcze nie spadł,",
      "ani błota z liści nie ma więc filcoków też nie zmieniasz.",
      "Idziesz sobie do 51 na systemy.",
      "Profesor ogląda cie wzrokiem i pyta o przeustkę.",
      "Jako że ty wogóle nie brałeś kurtki, to przepustka nie obowiązuje.",
      "",
      "Wchodzisz do sali 51."
    ], praktyka)

  selectDecision([
    "Piątek rano, już prawie weekend.",
    "",
    "Niestety od wolności dzieli cię jeszcze jeden dzień szkoły,",
    "a w nim Systemy z Klisiem.",
    "Budzisz się rano, wstajesz i ogarniasz się.",
    "Na zewnątrz jest 8 stopni, wydaje się być chłodno,",
    "ale zdarzało ci się chodzić w gorszych temperaturach.",
    "",
    "Chcesz brać kufajkę dla pewności i zdrowia,",
    "czy jesteś ciepły chłop i masz to gdzieś?"
  ], [
    ["Biorę kufajkę", kufajka1A],
    ["Nie biorę kufajki", kufajka1B]
  ])

kufajka()
