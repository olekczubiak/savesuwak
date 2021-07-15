# Save Suwak – Newonce🤐
Skrypt do zapisywania numerów pojawiających się w audycji "Funkowa środa Suwaka" w radiu Newonce. Dane są pobierane z API radia newonce. 
> https://newonce.net/api/radio_history 

Zapisane utwory są wysyłane na maila w celu lepszej organizacji. 

![](https://i.imgur.com/e7oAUc7.jpg)

### Env
Wykorzystana skrzynka pocztowa jest to **gmail**
W pliku env.py trzmane są dane do logowania do poczty:
```
SENDER_MAIL = 'example@gmail.com' # adres email z ktorego wysyłamy
PASSWORD = 'password' # Hasło do skrzynki pocztowej z której otrzymujemy dane
PORT = 587 - # port dla dla gmaila
SMTP_SERVER = 'smtp.gmail.com' # dla gmaila
RECIVER_MAIL = 'example@gmail.com' #adres na ktory wysyłamy składankę z dzisiaj
```
Jeżeli chcemy wysyłać na ten sam adres emailowy z którego wysyłamy, wystarczy dać ten sam adress co w **SENDER_MAIL**.

### Instalacja
Instalacje należy zacząć od zainstalowania biblioteki request. Następnie na serwerze za pomocą aplikacji **xxx** włączać skrypt main.py co środę w godzinach trwania audycji. 

