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
  time.sleep(3)
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
  def kufajka1A():
    def kufajka2A():
      nextQuest([
        "Zaniosłeś kufajkę do szatni.",
        "Przychodzisz do sali 51 i pokazujesz profesorowi przepustkę.",
        "Ten jeszcze szybko zerka na twoje buty i wpuszcza cię do sali."
      ], praktyka)

    def kufajka2B():
      def kufajka3A():
        nextQuest([
          "Odnosisz kufajkę do szatni, uzyskując przepustkę.",
          "Za jej pomocą jesteś w stanie wejść do sali 51 i zdążyć."
        ], praktyka)

      def kufajka3B():
        print("Olewasz frajera, co on ci bedzie rozkazywał.Plan był dobry, ale Kliś ruszył w pogoń za tobą. Wybiegasz z sali 51 i ganiasz się z Klisiem po terenie szkoły próbując go zgubić")
        # MINIGRA JAKAŚ JAK UCIEKNIESZ TO NIE TRAFIASZ NA PRAKTYKE MUSISZ NA DZIEN MIŁOSIEDZIA

      selectDecision([
        "Kliś przyłapał cię z kufajką na wejściu do sali.",
        "Nie udało ci się prześlizgnąć niezauważenie.",
        "Profesor rozkazuje Ci odnieść narzędzie zła na tej ziemi do szatni, ale co ty o tym sądzisz?"
      ], [
        ["Odnosisz kufajkę do szatni.", kufajka3A],
        ["Olewasz go.", kufajka3B]
      ])

    selectDecision([
      "Przychodzisz do szkoły na lekcje, prawie spóźniony boś gruby.",
      "Masz teraz zagadkę, zanieść kufajkę do szatni czy boisz się spóźnienia?"
    ], [
      ["Zanoszę", kufajka2A],
      ["Nie zanoszę", kufajka2B]
    ])

  selectDecision([
    "Budzisz się rano, wstajesz do szkoły.",
    "Na zewnątrz jest 15 stopni, dość chłodno ale co to dla ciebie.",
    "Chcesz brać kufajkę dla pewności czy jesteś ciepły chłop?"
  ], [
    ["Biorę kufajkę", kufajka1A],
    ["Nie biorę kufajki", praktyka]
  ])

kufajka()
