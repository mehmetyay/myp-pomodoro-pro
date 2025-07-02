import tkinter as tk
from tkinter import ttk, messagebox, font, Canvas, PhotoImage
import time
import winsound
import threading
from PIL import Image, ImageTk, ImageDraw
import sys
import json
import os
import datetime
from math import cos, sin, radians
import webbrowser
import random

class MYP_Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("MYP Premium Pomodoro Timer PRO")
        self.root.geometry("800x900")
        self.root.configure(bg="#1E1E2E")
        self.root.resizable(True, True)
        self.root.minsize(700, 800)
        
        # Uygulama bilgileri
        self.app_name = "MYP Pomodoro PRO"
        self.version = "2.0.0"
        self.author = "Mehmet Yay"
        self.license = "Proprietary"
        
        # Modern renk paleti
        self.colors = {
            "primary": "#7E57C2",
            "secondary": "#9575CD",
            "accent": "#B39DDB",
            "background": "#1E1E2E",
            "surface": "#2A2A3A",
            "text": "#E2E2E2",
            "error": "#EF5350",
            "success": "#66BB6A",
            "warning": "#FFA726"
        }
        # Yedekleme ayarları
        self.backup_count = 0
        self.backup_interval = 5  # Her 5 pomodoroda bir yedek al
        # Motivasyon mesajları
        self.motivational_messages = [
    "Harika gidiyorsun! Devam et!",
    "Odaklan, başaracaksın!",
    "Her pomodoro bir adım daha yaklaştırır",
    "Mola verdiğinde zihnini dinlendir",
    "Bugünün hedeflerine ulaşacaksın!",
    "Zamanını yönet, hayatını yönet!",
    "Küçük adımlar büyük zaferler getirir",
    "Şu anki çaban geleceğinin temelini atıyor",
    "Yorgunluk geçici, başarı kalıcıdır",
    "Beynin mola verdikçe daha iyi çalışır",
    "Disiplin, özgürlüğün bedelidir",
    "Şimdi odaklanma zamanı!",
    "Her tamamlanan görev bir zaferdir",
    "Zihnini dinlendir, yenilenmiş dön!",
    "Verimlilik senin süper gücün olsun",
    "Bu pomodoro senin altın dakikaların",
    "Dikkat dağıtıcıları uzaklaştır!",
    "Şu an yaptığın şeye tüm benliğini ver",
    "Mola vermek güç toplamaktır",
    "Bugünün işini yarına bırakma",
    "Sadece %1 daha fazla odaklan!",
    "Zorluklar seni güçlendiriyor",
    "Bir sonraki mola daha tatlı olacak",
    "Şu anki çaban gelecekteki seni gururlandıracak",
    "Her dakika önemli, boşa harcama!",
    "Beyin kaslarını çalıştırmaya devam et!",
    "Daha iyisi için kendini zorla!",
    "Başarılı insanların sırrı tutarlılıktır",
    "Yapabileceğinin en iyisini yapıyorsun!",
    "Mola zamanı! Gözlerini dinlendir",
    "Zihnini temizle, yeniden odaklan!",
    "Bu çalışma seansı çok verimli geçecek!",
    "Dikkatini koru, başaracaksın!",
    "Kendine söz verdiğin gibi devam et!",
    "Şimdi çalış, sonra rahatla!",
    "Üretkenlik moduna geç!",
    "Biraz daha dayan, hedefe yaklaşıyorsun!",
    "Bugün kendine yatırım yapıyorsun!",
    "Zamanın efendisi ol!",
    "Her görev bir fırsattır!",
    "Mola ver, ama pes etme!",
    "Konsantrasyon gücünü artır!",
    "Daha fazlasını başarabileceğini biliyorsun!",
    "Bu seansı en iyi şekilde değerlendir!",
    "Başarı merdivenlerini tek tek çıkıyorsun!",
    "Odaklan, tamamla, başar!",
    "Zihnini boşalt ve işe koyul!",
    "Her biten pomodoro seni hedefine yaklaştırır!",
    "Daha güçlü, daha odaklı!",
    "Şimdi iş zamanı!",
    "Mola zamanı! Ayağa kalk ve gerin!",
    "Beyin molası ver, verimliliğini artır!",
    "Kendini zorlamaya devam et!",
    "Başarıya giden yol disiplinden geçer!",
    "Şu an yaptığın her şey geleceğini şekillendiriyor!",
    "Daha fazla odak, daha az erteleme!",
    "Zamanını en iyi şekilde kullan!",
    "Her anını değerlendir!",
    "Bu pomodoro senin kontrolünde!",
    "Mola ver ama motivasyonunu kaybetme!",
    "Küçük molalar büyük başarılar getirir!",
    "Biraz daha devam et, hedefe çok yakınsın!",
    "Üretkenlik seninle olsun!",
    "Zihnini dinlendir, enerjini topla!",
    "Bugün harika işler başaracaksın!",
    "Odaklanma gücünü artırıyorsun!",
    "Her pomodoro seni daha iyiye götürür!",
    "Şimdi tam konsantrasyon zamanı!",
    "Mola ver ve zihnini tazele!",
    "Başarıya giden yolda bir adım daha!",
    "Daha fazla çaba, daha büyük başarı!",
    "Zamanını yönet, hayatını değiştir!",
    "Bu çalışma seansı çok verimli geçecek!",
    "Kendine güven, başaracaksın!",
    "Her görev bir fırsattır!",
    "Mola ver, ama asla vazgeçme!",
    "Konsantrasyon gücünü artır!",
    "Daha fazlasını başarabileceğini biliyorsun!",
    "Bu seansı en iyi şekilde değerlendir!",
    "Başarı merdivenlerini tek tek çıkıyorsun!",
    "Odaklan, tamamla, başar!",
    "Zihnini boşalt ve işe koyul!",
    "Her biten pomodoro seni hedefine yaklaştırır!",
    "Daha güçlü, daha odaklı!",
    "Şimdi iş zamanı!",
    "Mola zamanı! Ayağa kalk ve gerin!",
    "Beyin molası ver, verimliliğini artır!",
    "Kendini zorlamaya devam et!",
    "Başarıya giden yol disiplinden geçer!",
    "Şu an yaptığın her şey geleceğini şekillendiriyor!",
    "Daha fazla odak, daha az erteleme!",
    "Zamanını en iyi şekilde kullan!",
    "Her anını değerlendir!",
    "Bu pomodoro senin kontrolünde!",
    "Mola ver ama motivasyonunu kaybetme!",
    "Küçük molalar büyük başarılar getirir!",
    "Biraz daha devam et, hedefe çok yakınsın!",
    "Üretkenlik seninle olsun!",
    "Zihnini dinlendir, enerjini topla!",
    "Bugün harika işler başaracaksın!",
    "Odaklanma gücünü artırıyorsun!",
    "Her pomodoro seni daha iyiye götürür!",
    "Şimdi tam konsantrasyon zamanı!",
    "Mola ver ve zihnini tazele!",
    "Başarıya giden yolda bir adım daha!"      
        ]
        random.shuffle(self.motivational_messages)
        self.last_message_time = 0

        
        # Günlük hatırlatıcı kontrolü
        self.last_reminder_date = None
        self.check_daily_reminder()

        # Animasyon değişkenleri
        self.animation_angle = 0
        self.animation_running = False
        
        # Veri yapıları
        self.session_history = []
        self.tasks = []
        self.achievements = []
        self.settings = {
            "work_time": 25,
            "short_break": 5,
            "long_break": 15,
            "auto_start": False,
            "notifications": True,
            "dark_mode": True,
            "sounds": True,
            "target_pomodoros": 8
        }
        
        # Zaman yönetimi değişkenleri
        self.work_time = self.settings["work_time"] * 60
        self.break_time = self.settings["short_break"] * 60
        self.long_break_time = self.settings["long_break"] * 60
        self.current_time = self.work_time
        self.is_running = False
        self.is_work = True
        self.pomodoro_count = 0
        self.cycle_count = 0
        self.start_time = None
        self.total_productive_time = 0
        
        # UI öğeleri
        self.create_menu()
        self.create_ui()
        self.load_data()
        
        # Animasyon başlat
        self.start_animation()
        
    def check_daily_reminder(self):
        """Günlük hatırlatıcıyı kontrol et"""
        today = datetime.date.today()
        
        if self.last_reminder_date != today:
            current_hour = datetime.datetime.now().hour
            if 9 <= current_hour < 10:  # Sabah 9-10 arası
                self.show_notification("Bugünün planını oluşturdunuz mu? Görev eklemeyi unutmayın!")
                self.last_reminder_date = today
                
        # Her saat kontrol et
        self.root.after(3600000, self.check_daily_reminder)
        
    def create_menu(self):
        # Menü çubuğu oluştur
        menubar = tk.Menu(self.root)
        
        # Dosya menüsü
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Verileri Kaydet", command=self.save_data)
        file_menu.add_command(label="Verileri Yükle", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.quit_app)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        
        # Görünüm menüsü
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Koyu Tema", command=lambda: self.set_theme("dark"))
        view_menu.add_command(label="Açık Tema", command=lambda: self.set_theme("light"))
        menubar.add_cascade(label="Görünüm", menu=view_menu)
        
        # Yardım menüsü
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Kullanım Kılavuzu", command=self.show_help)
        help_menu.add_command(label="Hakkında", command=self.show_about)
        menubar.add_cascade(label="Yardım", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def create_backup(self):
        """Otomatik yedek oluştur"""
        try:
            # data/sessions klasörü yoksa oluştur
            os.makedirs("data/sessions", exist_ok=True)
            
            # Tarih damgası ile yedek dosyası
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"data/sessions/backup_{timestamp}.json"
            
            with open(backup_file, "w") as f:
                json.dump({
                    "session_history": self.session_history,
                    "tasks": self.tasks,
                    "stats": {
                        "total_productive_time": self.total_productive_time,
                        "pomodoro_count": self.pomodoro_count,
                        "cycle_count": self.cycle_count
                    }
                }, f, indent=4)
                
            if self.settings["notifications"]:
                self.show_notification(f"Otomatik yedek oluşturuldu: {backup_file}")
                
        except Exception as e:
            print(f"Yedekleme hatası: {e}")
    
    def create_ui(self):
        # Ana çerçeve
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Başlık alanı
        self.create_header()
        
        # Zaman göstergesi ve animasyon
        self.create_timer_display()
        
        # Kontrol paneli
        self.create_control_panel()
        
        # İlerleme çubukları
        self.create_progress_bars()
        
        # Görev yönetimi
        self.create_task_manager()
        
        # İstatistikler
        self.create_stats_section()
        
        # Ayarlar paneli
        self.create_settings_panel()
        
        # Stil ayarları
        self.configure_styles()
    


    def create_header(self):
        # Header frame oluşturuluyor
        header_frame = ttk.Frame(self.main_frame, style='Header.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))
    
        # Logo için dosya yolunu dinamik hale getiriyoruz
        base_path = os.path.dirname(os.path.abspath(__file__))  # Şu anki dosyanın bulunduğu dizini alır
        logo_path = os.path.join(base_path, "assets", "logo.png")  # assets klasörü içinde logo.png dosyası

        # Logo dosyasını aç ve boyutlandır
        try:
            self.logo_img = Image.open(logo_path).resize((50, 50))  # logo.jpeg dosyasını yükle ve boyutlandır
            self.logo_photo = ImageTk.PhotoImage(self.logo_img)
        except Exception as e:
            print(f"Logo yüklenemedi: {e}")
            return  # Logo yüklenemediği takdirde, fonksiyonu sonlandır
    
        # Logo'yu ekle
        logo_label = ttk.Label(header_frame, image=self.logo_photo, style='Header.TLabel')
        logo_label.image = self.logo_photo  # Referansı koru
        logo_label.pack(side=tk.LEFT, padx=(10, 20))
    
        # Başlık için daha modern bir düzen
        title_frame = ttk.Frame(header_frame, style='Header.TFrame')
        title_frame.pack(side=tk.LEFT)
    
        # Başlık metni
        title_label = ttk.Label(title_frame, 
                            text="MYP POMODORO PRO", 
                            style='Header.TLabel',
                            font=('Segoe UI', 20, 'bold'))
        title_label.pack(anchor='w')
    
        # Alt başlık
        subtitle_label = ttk.Label(title_frame,
                               text="Premium Productivity Timer",
                               style='Secondary.TLabel',
                               font=('Segoe UI', 10))
        subtitle_label.pack(anchor='w')
    
        # Versiyon bilgisi
        version_label = ttk.Label(header_frame, 
                              text=f"v{self.version}", 
                              style='Secondary.TLabel')
        version_label.pack(side=tk.RIGHT, anchor='ne')

    
    def create_timer_display(self):
        timer_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        timer_frame.pack(fill=tk.X, pady=(0, 20), ipady=10)
        
        # Zaman göstergesi
        self.time_label = ttk.Label(timer_frame, 
                                  text=self.format_time(self.current_time), 
                                  style='Timer.TLabel')
        self.time_label.pack(pady=(10, 5))
        
        # Durum bilgisi
        self.status_label = ttk.Label(timer_frame, 
                                    text="Çalışma Zamanı", 
                                    style='Status.TLabel')
        self.status_label.pack(pady=(0, 10))
        
        # Pomodoro sayacı
        pomodoro_frame = ttk.Frame(timer_frame, style='Card.TFrame')
        pomodoro_frame.pack(pady=(0, 10))
        
        self.pomodoro_labels = []
        for i in range(4):
            label = ttk.Label(pomodoro_frame, text="●", 
                            style='PomodoroInactive.TLabel' if i > 0 else 'PomodoroActive.TLabel')
            label.pack(side=tk.LEFT, padx=5)
            self.pomodoro_labels.append(label)
        
        # Animasyon canvas
        self.animation_canvas = Canvas(timer_frame, width=200, height=20, bg=self.colors["surface"], highlightthickness=0)
        self.animation_canvas.pack(pady=(5, 0))
    
    def create_control_panel(self):
        control_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        control_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Kontrol butonları
        btn_frame = ttk.Frame(control_frame, style='Card.TFrame')
        btn_frame.pack(pady=10)
        
        # 3D efektli butonlar
        self.start_btn = self.create_3d_button(btn_frame, "Başlat", self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=10)
        
        self.pause_btn = self.create_3d_button(btn_frame, "Duraklat", self.pause_timer, state=tk.DISABLED)
        self.pause_btn.grid(row=0, column=1, padx=10)
        
        self.reset_btn = self.create_3d_button(btn_frame, "Sıfırla", self.reset_timer)
        self.reset_btn.grid(row=0, column=2, padx=10)
        
        self.skip_btn = self.create_3d_button(btn_frame, "Geç", self.skip_timer)
        self.skip_btn.grid(row=0, column=3, padx=10)
    
    def create_progress_bars(self):
        progress_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Günlük ilerleme
        ttk.Label(progress_frame, text="Günlük İlerleme", style='SectionTitle.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        
        self.daily_progress = ttk.Progressbar(progress_frame, 
                                            orient=tk.HORIZONTAL, 
                                            length=100, 
                                            mode='determinate',
                                            maximum=self.settings["target_pomodoros"])
        self.daily_progress.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Haftalık ilerleme
        ttk.Label(progress_frame, text="Haftalık İlerleme", style='SectionTitle.TLabel').pack(anchor='w', padx=10, pady=(5, 5))
        
        self.weekly_progress = ttk.Progressbar(progress_frame, 
                                             orient=tk.HORIZONTAL, 
                                             length=100, 
                                             mode='determinate',
                                             maximum=7*self.settings["target_pomodoros"])
        self.weekly_progress.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # İlerleme etiketleri
        self.progress_labels = ttk.Frame(progress_frame, style='Card.TFrame')
        self.progress_labels.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Label(self.progress_labels, text="Bugün:", style='ProgressLabel.TLabel').grid(row=0, column=0, sticky='w')
        self.today_label = ttk.Label(self.progress_labels, text="0/8", style='ProgressValue.TLabel')
        self.today_label.grid(row=0, column=1, sticky='e', padx=10)
        
        ttk.Label(self.progress_labels, text="Bu Hafta:", style='ProgressLabel.TLabel').grid(row=1, column=0, sticky='w', pady=(5, 0))
        self.week_label = ttk.Label(self.progress_labels, text="0/56", style='ProgressValue.TLabel')
        self.week_label.grid(row=1, column=1, sticky='e', padx=10, pady=(5, 0))
    
    def create_task_manager(self):
        task_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        task_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Başlık
        ttk.Label(task_frame, text="Görev Yönetimi", style='SectionTitle.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        
        # Görev giriş alanı
        input_frame = ttk.Frame(task_frame, style='Card.TFrame')
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.task_entry = ttk.Entry(input_frame, font=('Helvetica', 10))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        add_btn = self.create_3d_button(input_frame, "Ekle", self.add_task, width=10)
        add_btn.pack(side=tk.RIGHT)
        
        # Görev listesi
        self.task_listbox = tk.Listbox(task_frame, 
                                     bg=self.colors["surface"], 
                                     fg=self.colors["text"], 
                                     selectbackground=self.colors["primary"],
                                     font=('Helvetica', 10),
                                     height=5,
                                     relief=tk.FLAT)
        self.task_listbox.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Görev kontrolleri
        task_btn_frame = ttk.Frame(task_frame, style='Card.TFrame')
        task_btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        complete_btn = self.create_3d_button(task_btn_frame, "Tamamlandı", self.complete_task, width=12)
        complete_btn.grid(row=0, column=0, padx=(0, 5))
        
        delete_btn = self.create_3d_button(task_btn_frame, "Sil", self.delete_task, width=8)
        delete_btn.grid(row=0, column=1, padx=5)
        
        clear_btn = self.create_3d_button(task_btn_frame, "Temizle", self.clear_tasks, width=8)
        clear_btn.grid(row=0, column=2, padx=(5, 0))
    
    def create_stats_section(self):
        stats_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Başlık
        ttk.Label(stats_frame, text="İstatistikler", style='SectionTitle.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        
        # İstatistik kartları
        cards_frame = ttk.Frame(stats_frame, style='Card.TFrame')
        cards_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Bugünkü pomodorolar
        today_card = ttk.Frame(cards_frame, style='StatCard.TFrame')
        today_card.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        
        ttk.Label(today_card, text="Bugün", style='StatTitle.TLabel').pack()
        self.today_stat = ttk.Label(today_card, text="0", style='StatValue.TLabel')
        self.today_stat.pack()
        ttk.Label(today_card, text="Pomodoro", style='StatUnit.TLabel').pack()
        
        # Bu haftaki pomodorolar
        week_card = ttk.Frame(cards_frame, style='StatCard.TFrame')
        week_card.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        ttk.Label(week_card, text="Bu Hafta", style='StatTitle.TLabel').pack()
        self.week_stat = ttk.Label(week_card, text="0", style='StatValue.TLabel')
        self.week_stat.pack()
        ttk.Label(week_card, text="Pomodoro", style='StatUnit.TLabel').pack()
        
        # Toplam üretken zaman
        time_card = ttk.Frame(cards_frame, style='StatCard.TFrame')
        time_card.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        
        ttk.Label(time_card, text="Toplam", style='StatTitle.TLabel').pack()
        self.time_stat = ttk.Label(time_card, text="0h 0m", style='StatValue.TLabel')
        self.time_stat.pack()
        ttk.Label(time_card, text="Üretken Zaman", style='StatUnit.TLabel').pack()
        
        # Döngüler
        cycle_card = ttk.Frame(cards_frame, style='StatCard.TFrame')
        cycle_card.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')
        
        ttk.Label(cycle_card, text="Tam", style='StatTitle.TLabel').pack()
        self.cycle_stat = ttk.Label(cycle_card, text="0", style='StatValue.TLabel')
        self.cycle_stat.pack()
        ttk.Label(cycle_card, text="Döngü", style='StatUnit.TLabel').pack()
        
        # Eşit boyut için
        cards_frame.columnconfigure(0, weight=1)
        cards_frame.columnconfigure(1, weight=1)
        cards_frame.columnconfigure(2, weight=1)
        cards_frame.columnconfigure(3, weight=1)
    
    def create_settings_panel(self):
        settings_frame = ttk.Frame(self.main_frame, style='Card.TFrame')
        settings_frame.pack(fill=tk.X)
        
        # Başlık
        ttk.Label(settings_frame, text="Ayarlar", style='SectionTitle.TLabel').pack(anchor='w', padx=10, pady=(10, 5))
        
        # Ayarlar grid
        grid_frame = ttk.Frame(settings_frame, style='Card.TFrame')
        grid_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        ttk.Label(grid_frame, text="Özel Çalışma Süresi (dk):", style='SettingLabel.TLabel').grid(row=4, column=0, sticky='w', pady=2)
        self.custom_work_entry = ttk.Spinbox(grid_frame, from_=1, to=180, width=5)
        self.custom_work_entry.set(45)  # Varsayılan değer
        self.custom_work_entry.grid(row=4, column=1, sticky='e', pady=2, padx=5)
    
        ttk.Label(grid_frame, text="Özel Mola Süresi (dk):", style='SettingLabel.TLabel').grid(row=5, column=0, sticky='w', pady=2)
        self.custom_break_entry = ttk.Spinbox(grid_frame, from_=1, to=60, width=5)
        self.custom_break_entry.set(10)  # Varsayılan değer
        self.custom_break_entry.grid(row=5, column=1, sticky='e', pady=2, padx=5)
    
        # Mod seçimi için Radiobutton'lar
        ttk.Label(grid_frame, text="Çalışma Modu:", style='SettingLabel.TLabel').grid(row=6, column=0, sticky='w', pady=2)
        self.mode_var = tk.StringVar(value="classic")  # Varsayılan klasik mod
    
        mode_frame = ttk.Frame(grid_frame, style='Card.TFrame')
        mode_frame.grid(row=6, column=1, sticky='ew', pady=2)
    
        ttk.Radiobutton(mode_frame, text="Klasik", variable=self.mode_var, 
                   value="classic", style='Toggle.TRadiobutton').pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text="Özel", variable=self.mode_var, 
                   value="custom", style='Toggle.TRadiobutton').pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text="Yoğun", variable=self.mode_var, 
                   value="intense", style='Toggle.TRadiobutton').pack(side=tk.LEFT)
        
        # Çalışma süresi
        ttk.Label(grid_frame, text="Çalışma Süresi (dk):", style='SettingLabel.TLabel').grid(row=0, column=0, sticky='w', pady=2)
        self.work_entry = ttk.Spinbox(grid_frame, from_=1, to=120, width=5)
        self.work_entry.set(self.settings["work_time"])
        self.work_entry.grid(row=0, column=1, sticky='e', pady=2, padx=5)
        
        # Kısa mola
        ttk.Label(grid_frame, text="Kısa Mola (dk):", style='SettingLabel.TLabel').grid(row=1, column=0, sticky='w', pady=2)
        self.short_break_entry = ttk.Spinbox(grid_frame, from_=1, to=30, width=5)
        self.short_break_entry.set(self.settings["short_break"])
        self.short_break_entry.grid(row=1, column=1, sticky='e', pady=2, padx=5)
        
        # Uzun mola
        ttk.Label(grid_frame, text="Uzun Mola (dk):", style='SettingLabel.TLabel').grid(row=2, column=0, sticky='w', pady=2)
        self.long_break_entry = ttk.Spinbox(grid_frame, from_=1, to=60, width=5)
        self.long_break_entry.set(self.settings["long_break"])
        self.long_break_entry.grid(row=2, column=1, sticky='e', pady=2, padx=5)
        
        # Hedef pomodorolar
        ttk.Label(grid_frame, text="Günlük Hedef:", style='SettingLabel.TLabel').grid(row=3, column=0, sticky='w', pady=2)
        self.target_entry = ttk.Spinbox(grid_frame, from_=1, to=20, width=5)
        self.target_entry.set(self.settings["target_pomodoros"])
        self.target_entry.grid(row=3, column=1, sticky='e', pady=2, padx=5)
        
        # Diğer ayarlar
        settings_btn_frame = ttk.Frame(settings_frame, style='Card.TFrame')
        settings_btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.auto_start_var = tk.BooleanVar(value=self.settings["auto_start"])
        auto_start_cb = ttk.Checkbutton(settings_btn_frame, 
                                       text="Otomatik Başlat", 
                                       variable=self.auto_start_var,
                                       style='Toggle.TCheckbutton')
        auto_start_cb.grid(row=0, column=0, sticky='w', padx=5)
        
        self.notifications_var = tk.BooleanVar(value=self.settings["notifications"])
        notifications_cb = ttk.Checkbutton(settings_btn_frame, 
                                          text="Bildirimler", 
                                          variable=self.notifications_var,
                                          style='Toggle.TCheckbutton')
        notifications_cb.grid(row=0, column=1, sticky='w', padx=5)
        
        self.sounds_var = tk.BooleanVar(value=self.settings["sounds"])
        sounds_cb = ttk.Checkbutton(settings_btn_frame, 
                                  text="Sesler", 
                                  variable=self.sounds_var,
                                  style='Toggle.TCheckbutton')
        sounds_cb.grid(row=0, column=2, sticky='w', padx=5)
        
        # Uygula butonu
        apply_btn = self.create_3d_button(settings_frame, "Ayarları Uygula", self.apply_settings, width=20)
        apply_btn.pack(pady=(0, 10))
    
    def configure_styles(self):
        # Temel stiller
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Arka plan stilleri
        self.style.configure('.', background=self.colors["background"], foreground=self.colors["text"])
        
        # Frame stilleri
        self.style.configure('TFrame', background=self.colors["background"])
        self.style.configure('Card.TFrame', background=self.colors["surface"], relief=tk.RAISED, borderwidth=1)
        self.style.configure('Header.TFrame', background=self.colors["primary"])
        self.style.configure('StatCard.TFrame', background=self.colors["surface"], relief=tk.RAISED, borderwidth=1)
        
        # Label stilleri
        self.style.configure('TLabel', background=self.colors["background"], foreground=self.colors["text"])
        self.style.configure('Header.TLabel', background=self.colors["primary"], foreground='white', font=('Helvetica', 18, 'bold'))
        self.style.configure('Secondary.TLabel', background=self.colors["background"], foreground=self.colors["accent"])
        self.style.configure('Timer.TLabel', font=('Helvetica', 48, 'bold'), foreground=self.colors["primary"])
        self.style.configure('Status.TLabel', font=('Helvetica', 14, 'bold'), foreground=self.colors["accent"])
        self.style.configure('SectionTitle.TLabel', font=('Helvetica', 12, 'bold'), foreground=self.colors["primary"])
        self.style.configure('ProgressLabel.TLabel', font=('Helvetica', 10))
        self.style.configure('ProgressValue.TLabel', font=('Helvetica', 10, 'bold'), foreground=self.colors["primary"])
        self.style.configure('StatTitle.TLabel', font=('Helvetica', 10), foreground=self.colors["accent"])
        self.style.configure('StatValue.TLabel', font=('Helvetica', 18, 'bold'), foreground=self.colors["primary"])
        self.style.configure('StatUnit.TLabel', font=('Helvetica', 8), foreground=self.colors["text"])
        self.style.configure('SettingLabel.TLabel', font=('Helvetica', 10))
        self.style.configure('PomodoroActive.TLabel', font=('Helvetica', 14), foreground=self.colors["success"])
        self.style.configure('PomodoroInactive.TLabel', font=('Helvetica', 14), foreground=self.colors["surface"])
        
        # Buton stilleri
        self.style.configure('TButton', 
                           background=self.colors["secondary"], 
                           foreground='white',
                           font=('Helvetica', 10, 'bold'),
                           borderwidth=1,
                           relief=tk.RAISED)
        self.style.map('TButton', 
                      background=[('active', self.colors["primary"]), ('disabled', self.colors["surface"])],
                      foreground=[('active', 'white'), ('disabled', self.colors["text"])])
        
        # Progressbar stilleri
        self.style.configure('Horizontal.TProgressbar', 
                           background=self.colors["primary"],
                           troughcolor=self.colors["surface"],
                           bordercolor=self.colors["background"],
                           lightcolor=self.colors["accent"],
                           darkcolor=self.colors["primary"])
        
        # Entry stilleri
        self.style.configure('TEntry', 
                           fieldbackground=self.colors["surface"],
                           foreground=self.colors["text"],
                           insertcolor=self.colors["text"],
                           relief=tk.FLAT)
        
        # Checkbutton stilleri
        self.style.configure('Toggle.TCheckbutton', 
                           background=self.colors["surface"],
                           foreground=self.colors["text"],
                           indicatorbackground=self.colors["surface"],
                           indicatordiameter=15)
        self.style.map('Toggle.TCheckbutton', 
                      background=[('active', self.colors["surface"])])
        
        # Listbox stili
        self.style.configure('TListbox', 
                           background=self.colors["surface"],
                           foreground=self.colors["text"],
                           selectbackground=self.colors["primary"],
                           selectforeground='white',
                           relief=tk.FLAT)
    
    def create_3d_button(self, parent, text, command, width=None, state=tk.NORMAL):
        # 3D efektli buton oluşturma
        btn = ttk.Button(parent, 
                        text=text, 
                        command=command, 
                        style='TButton',
                        width=width,
                        state=state)
        
        # Hover efekti için bağlantılar
        btn.bind("<Enter>", lambda e: btn.config(style='Hover.TButton'))
        btn.bind("<Leave>", lambda e: btn.config(style='TButton'))
        
        return btn
    
    def start_animation(self):
        self.animation_running = True
        self.animate()
    
    def stop_animation(self):
        self.animation_running = False
    
    def animate(self):
        if not self.animation_running:
            return
            
        self.animation_angle = (self.animation_angle + 5) % 360
        self.draw_animation()
        self.root.after(50, self.animate)
    
    def draw_animation(self):
        self.animation_canvas.delete("all")
        width = self.animation_canvas.winfo_width()
        height = self.animation_canvas.winfo_height()
    
        # Dalga animasyonu
        points = []
        for x in range(0, width+1, 5):
            y = height / 2 + sin(radians(x * 2 + self.animation_angle)) * (height / 4)
            points.append(x)  # X koordinatlarını ekle
            points.append(y)  # Y koordinatlarını ekle

        # points'in en az 4 koordinat içerdiğinden emin ol
        if len(points) >= 4:
            self.animation_canvas.create_line(points, fill=self.colors["primary"], width=2, smooth=True)

    
    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_timer(self):
        if self.is_running and self.current_time > 0:
            self.current_time -= 1
            self.time_label.config(text=self.format_time(self.current_time))

            # Every 5 minutes (300, 600, 900... seconds remaining)
            if self.current_time % 300 == 0:
                self.show_random_message()

            self.root.after(1000, self.update_timer)
        elif self.current_time == 0:
            self.timer_complete()


            
    
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.start_btn.config(state=tk.DISABLED)
            self.pause_btn.config(state=tk.NORMAL)
            self.update_timer()
            
            # Çalışma modunda görev hatırlatıcı
            if self.is_work and self.task_listbox.size() > 0:
                current_task = self.task_listbox.get(0)
                self.show_notification(f"Şu anki görev: {current_task}")
    
    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.total_productive_time += time.time() - self.start_time
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED)
    
    def reset_timer(self):
        self.is_running = False
        self.current_time = self.work_time if self.is_work else (self.long_break_time if self.pomodoro_count % 4 == 0 else self.break_time)
        self.time_label.config(text=self.format_time(self.current_time))
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Çalışma Zamanı" if self.is_work else "Mola Zamanı")
    
    def skip_timer(self):
        self.timer_complete()
    
    def timer_complete(self):
        self.is_running = False
        
        # Üretken zamanı güncelle
        if self.start_time:
            self.total_productive_time += time.time() - self.start_time
            self.start_time = None
        
        # Ses çal
        if self.settings["sounds"]:
            self.play_alarm()
        
        if self.is_work:
            self.pomodoro_count += 1
            # Yedekleme kontrolü
            self.backup_count += 1
            if self.backup_count >= self.backup_interval:
                self.create_backup()
                self.backup_count = 0
            self.session_history.append({
                "type": "work",
                "duration": self.work_time,
                "timestamp": datetime.datetime.now().isoformat()
            })
            
            if self.pomodoro_count % 4 == 0:
                self.cycle_count += 1
                if self.settings["notifications"]:
                    self.show_notification("Uzun molaya çıkma zamanı!")
                self.current_time = self.long_break_time
            else:
                if self.settings["notifications"]:
                    self.show_notification("Kısa molaya çıkma zamanı!")
                self.current_time = self.break_time
        else:
            self.session_history.append({
                "type": "break",
                "duration": self.long_break_time if self.pomodoro_count % 4 == 0 else self.break_time,
                "timestamp": datetime.datetime.now().isoformat()
            })
            
            if self.settings["notifications"]:
                self.show_notification("Çalışma zamanı!")
            self.current_time = self.work_time
            
        self.is_work = not self.is_work
        self.update_status()
        self.update_stats()
        self.update_pomodoro_indicators()
        self.reset_timer()
        
        # Otomatik başlatma
        if self.settings["auto_start"]:
            self.start_timer()
    
    def play_alarm(self):
        def _play():
            for i in range(3):
                winsound.Beep(1000 + i*200, 300)
                time.sleep(0.3)
        
        threading.Thread(target=_play, daemon=True).start()
    
    def show_notification(self, message):
        # Basit bir bildirim penceresi
        notification = tk.Toplevel(self.root)
        notification.title("Bildirim")
        notification.geometry("300x100")
        notification.resizable(False, False)
        notification.configure(bg=self.colors["surface"])
        
        # Pozisyon ayarla (sağ alt köşe)
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        notification.geometry(f"+{root_x + root_width - 320}+{root_y + 50}")
        
        # İçerik
        label = ttk.Label(notification, text=message, style='Notification.TLabel')
        label.pack(expand=True, padx=20, pady=20)
        
        # 3 saniye sonra kapat
        notification.after(3000, notification.destroy)
    
    def update_status(self):
        if self.is_work:
            self.status_label.config(text="Çalışma Zamanı", style='Status.TLabel')
        else:
            if self.pomodoro_count % 4 == 0:
                self.status_label.config(text="Uzun Mola Zamanı", style='Status.TLabel')
            else:
                self.status_label.config(text="Mola Zamanı", style='Status.TLabel')
    
    def update_pomodoro_indicators(self):
        for i in range(4):
            if i < self.pomodoro_count % 4:
                self.pomodoro_labels[i].config(style='PomodoroActive.TLabel')
            else:
                self.pomodoro_labels[i].config(style='PomodoroInactive.TLabel')
    
    def update_stats(self):
        # Günlük ilerleme
        today_pomodoros = sum(1 for session in self.session_history 
                            if session["type"] == "work" and 
                            datetime.datetime.fromisoformat(session["timestamp"]).date() == datetime.date.today())
        
        self.daily_progress['value'] = today_pomodoros
        self.today_label.config(text=f"{today_pomodoros}/{self.settings['target_pomodoros']}")
        
        # Haftalık ilerleme
        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())
        weekly_pomodoros = sum(1 for session in self.session_history 
                              if session["type"] == "work" and 
                              datetime.datetime.fromisoformat(session["timestamp"]).date() >= start_of_week)
        
        self.weekly_progress['value'] = weekly_pomodoros
        self.week_label.config(text=f"{weekly_pomodoros}/{7*self.settings['target_pomodoros']}")
        
        # İstatistik kartları
        self.today_stat.config(text=str(today_pomodoros))
        self.week_stat.config(text=str(weekly_pomodoros))
        
        total_hours = int(self.total_productive_time // 3600)
        total_minutes = int((self.total_productive_time % 3600) // 60)
        self.time_stat.config(text=f"{total_hours}h {total_minutes}m")
        
        self.cycle_stat.config(text=str(self.cycle_count))
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({
                "text": task,
                "completed": False,
                "created": datetime.datetime.now().isoformat()
            })
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_data()
    
    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]["completed"] = True
            self.tasks[index]["completed_at"] = datetime.datetime.now().isoformat()
            self.task_listbox.delete(index)
            self.save_data()
            
            # Tamamlanan görev bildirimi
            if self.settings["notifications"]:
                self.show_notification("Görev tamamlandı! 🎉")
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
            self.save_data()
    
    def clear_tasks(self):
        self.tasks = [task for task in self.tasks if task["completed"]]
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if not task["completed"]:
                self.task_listbox.insert(tk.END, task["text"])
        self.save_data()
    
    def apply_settings(self):
        try:
            new_work = int(self.work_entry.get())
            new_short_break = int(self.short_break_entry.get())
            new_long_break = int(self.long_break_entry.get())
            new_target = int(self.target_entry.get())
            
            if new_work <= 0 or new_short_break <= 0 or new_long_break <= 0 or new_target <= 0:
             raise ValueError("All values must be positive integers")
            
            # Yeni eklenen özel zaman ayarları
            custom_work = int(self.custom_work_entry.get())
            custom_break = int(self.custom_break_entry.get())
            selected_mode = self.mode_var.get()
        
            # Moda göre zamanları ayarla
            if selected_mode == "classic":
                self.work_time = new_work * 60
                self.break_time = new_short_break * 60
            elif selected_mode == "custom":
                self.work_time = custom_work * 60
                self.break_time = custom_break * 60
            elif selected_mode == "intense":  # Yoğun mod: 50/10 dk
                self.work_time = 50 * 60
                self.break_time = 10 * 60
            
            # Update settings
            self.settings["work_time"] = new_work
            self.settings["short_break"] = new_short_break
            self.settings["long_break"] = new_long_break
            self.settings["target_pomodoros"] = new_target
            self.settings["auto_start"] = self.auto_start_var.get()
            self.settings["notifications"] = self.notifications_var.get()
            self.settings["sounds"] = self.sounds_var.get()
            
            # Update timer values
            self.work_time = new_work * 60
            self.break_time = new_short_break * 60
            self.long_break_time = new_long_break * 60
            
            # Update progress bars max values
            self.daily_progress['maximum'] = new_target
            self.weekly_progress['maximum'] = 7 * new_target
            self.week_label.config(text=f"0/{7*new_target}")
            
            # Reset timer if not running
            if not self.is_running:
                self.reset_timer()
            
            # Save settings
            self.save_data()
            
            # Show success message
            messagebox.showinfo("Başarılı", "Ayarlar başarıyla güncellendi!")
            
        except ValueError as e:
            messagebox.showerror("Hata", f"Geçersiz değer: {str(e)}")
    
    def set_theme(self, theme):
        if theme == "dark":
            self.colors = {
                "primary": "#7E57C2",
                "secondary": "#9575CD",
                "accent": "#B39DDB",
                "background": "#1E1E2E",
                "surface": "#2A2A3A",
                "text": "#E2E2E2",
                "error": "#EF5350",
                "success": "#66BB6A",
                "warning": "#FFA726"
            }
        else:
            self.colors = {
                "primary": "#5E35B1",
                "secondary": "#7E57C2",
                "accent": "#B39DDB",
                "background": "#FAFAFA",
                "surface": "#FFFFFF",
                "text": "#212121",
                "error": "#D32F2F",
                "success": "#388E3C",
                "warning": "#F57C00"
            }
        
        # Reconfigure styles
        self.configure_styles()
        
        # Update all UI elements
        self.update_ui_colors()
        
        # Save theme preference
        self.settings["dark_mode"] = (theme == "dark")
        self.save_data()
    
    def update_ui_colors(self):
        """Update all UI elements with new colors"""
        # Update main window
        self.root.configure(bg=self.colors["background"])
        
        # Update timer display
        self.time_label.config(foreground=self.colors["primary"])
        self.status_label.config(foreground=self.colors["accent"])
        
        # Update animation canvas
        self.animation_canvas.config(bg=self.colors["surface"])
        
        # Update task listbox
        self.task_listbox.config(
            bg=self.colors["surface"],
            fg=self.colors["text"],
            selectbackground=self.colors["primary"]
        )
    
    def save_data(self):
        """Save all application data to file"""
        data = {
            "settings": self.settings,
            "tasks": self.tasks,
            "session_history": self.session_history,
            "achievements": self.achievements,
            "total_productive_time": self.total_productive_time,
            "pomodoro_count": self.pomodoro_count,
            "cycle_count": self.cycle_count
        }
        
        try:
            with open("pomodoro_data.json", "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Hata", f"Veri kaydedilirken hata oluştu: {str(e)}")
    
    def load_data(self):
        """Load application data from file"""
        try:
            if os.path.exists("pomodoro_data.json"):
                with open("pomodoro_data.json", "r") as f:
                    data = json.load(f)
                    
                    self.settings = data.get("settings", self.settings)
                    self.tasks = data.get("tasks", [])
                    self.session_history = data.get("session_history", [])
                    self.achievements = data.get("achievements", [])
                    self.total_productive_time = data.get("total_productive_time", 0)
                    self.pomodoro_count = data.get("pomodoro_count", 0)
                    self.cycle_count = data.get("cycle_count", 0)
                    
                    # Update UI elements
                    self.work_entry.set(self.settings["work_time"])
                    self.short_break_entry.set(self.settings["short_break"])
                    self.long_break_entry.set(self.settings["long_break"])
                    self.target_entry.set(self.settings["target_pomodoros"])
                    self.auto_start_var.set(self.settings["auto_start"])
                    self.notifications_var.set(self.settings["notifications"])
                    self.sounds_var.set(self.settings["sounds"])
                    
                    # Update timer values
                    self.work_time = self.settings["work_time"] * 60
                    self.break_time = self.settings["short_break"] * 60
                    self.long_break_time = self.settings["long_break"] * 60
                    
                    # Update progress bars
                    self.daily_progress['maximum'] = self.settings["target_pomodoros"]
                    self.weekly_progress['maximum'] = 7 * self.settings["target_pomodoros"]
                    
                    # Load tasks
                    self.task_listbox.delete(0, tk.END)
                    for task in self.tasks:
                        if not task.get("completed", False):
                            self.task_listbox.insert(tk.END, task["text"])
                    
                    # Update stats
                    self.update_stats()
                    
                    # Set theme
                    self.set_theme("dark" if self.settings.get("dark_mode", True) else "light")
                    
        except Exception as e:
            messagebox.showerror("Hata", f"Veri yüklenirken hata oluştu: {str(e)}")
    
    def show_help(self):
        """Show help documentation"""
        help_text = """
        MYP Pomodoro Timer PRO Kullanım Kılavuzu
        
        1. Çalışma Süresi: Odaklanmak istediğiniz süre (varsayılan: 25 dakika)
        2. Kısa Mola: Kısa molalar için süre (varsayılan: 5 dakika)
        3. Uzun Mola: 4 pomodoro sonrası uzun mola (varsayılan: 15 dakika)
        
        Özellikler:
        - Görev yönetimi
        - İstatistik takibi
        - Özelleştirilebilir ayarlar
        - Koyu/açık tema desteği
        """
        messagebox.showinfo("Yardım", help_text)
    
    def show_about(self):
        """Show about dialog"""
        about_text = f"""
        {self.app_name} v{self.version}
        
        Geliştirici: {self.author}
        Lisans: {self.license}
        
        Pomodoro tekniği ile verimliliğinizi artırın!
        """
        messagebox.showinfo("Hakkında", about_text)

    def show_random_message(self):
        """Rastgele motivasyon mesajı göster"""
        if self.settings["notifications"] and self.is_work:
            import random
            message = random.choice(self.motivational_messages)
            self.show_notification(message)
    
    def quit_app(self):
        """Quit application with confirmation"""
        if messagebox.askokcancel("Çıkış", "Uygulamadan çıkmak istediğinize emin misiniz?"):
            self.save_data()
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MYP_Pomodoro(root)
    root.mainloop()