class TV:
    def __init__(self):
        self.state = "On"
        self.current_channel = 1

    def power_on_off(self):
        if self.state == "Off":
            print("TV ligada")
            self.state = "On"
        else:
            print("TV desligada")
            self.state = "Off"

    def change_channel(self, channel):
        self.current_channel = channel
        print(f"Canal alterado para canal número {channel}")
        
    def show_current_channel(self):
        print(f"Atualmente no canal número {self.current_channel}")

    def open_netflix(self):
        print("Netflix aberto")

    def open_spotify(self):
        print("Spotify aberto")

class SoundSystem:
    def __init__(self):
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 10
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume no máximo")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 10
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume no mínimo")
            
    def current_volume(self):
        print(f"Atualmente no volume {self.volume}")

class UniversalRemoteControl:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()

    def show_menu(self):
        print("Escolha um dispositivo:")
        print("1. TV")
        print("2. SoundSystem")

    def press_button(self):
        self.show_menu()
        choice = input("Selecione o número do dispositivo que deseja controlar (1-2): ")

        if choice == '1':
            device = "TV"
        elif choice == '2':
            device = "SoundSystem"
        else:
            print("Por favor escolha uma opção válida.")
            return

        print(f"Selecione uma ação para {device}:")
        if device == "TV":
            print("1. Power On/Off")
            print("2. Mudar Canal")
            print("3. Exibir Canal Atual")
            print("4. Abrir Netflix")
            print("5. Abrir Spotify")
        elif device == "SoundSystem":
            print("1. Aumentar Volume")
            print("2. Diminuir Volume")
            print("3. Exibir Volume Atual")

        action_choice = input("Aperte o número da ação que você deseja realizar: ")
        if device == "TV" and action_choice == '1':
            self.tv.power_on_off()
        elif device == "TV" and action_choice == '2':
            new_channel = int(input("Digite o número do canal desejado: "))
            self.tv.change_channel(new_channel)
        elif device == "TV" and action_choice == '3':
            self.tv.show_current_channel()
        elif device == "TV" and action_choice == '4':
            self.tv.open_netflix()
        elif device == "TV" and action_choice == '5':
            self.tv.open_spotify()
        elif device == "SoundSystem" and action_choice == '1':
            self.sound_system.increase_volume()
        elif device == "SoundSystem" and action_choice == '2':
            self.sound_system.decrease_volume()
        elif device == "SoundSystem" and action_choice == '3':
            self.sound_system.current_volume()
        else:
            print("Ação Inválida. Por favor selecione uma ação válida.")

# Exemplo de uso
remote = UniversalRemoteControl()
while True:
    if remote.tv.state == "Off":
        break

    remote.press_button()