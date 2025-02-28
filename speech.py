# Bu komut bizim ses dosyalarımızı transkripsion işlemimizi yaplamak adına içeri aktarılan komuttur.
import speech_recognition as sr
"""
    #Mikrofon değerini bir değişkenin içerisine atamak
    mic = sr.Microphone()
    #Analog formatta ses Kaydının kaydedildiği değişken:
    recog = sr.Recognizer()

    # Bir mikrofon nesnesini (mic) alarak, bu nesneyi kullanarak ses kaydı yapacağımız bir ortam oluşturur
    # Bu sayede, kod bloğu tamamlandığında mikrofon otomatik olarak kapatılır.
    with mic as audio_file:
        print('Lütfen Konuşun...')
        # Mikrofon üzerinden alınan ilk ses kayıtlarını kullanarak ortam gürültüsünü analiz eder. 
        # Bu sayede, daha sonraki ses kayıtlarında ortam gürültüsünün etkisi azaltılır.
        recog.adjust_for_ambient_noise(audio_file)
        # Analog Formattan Sesin Dijital Ortama Aktarılması işidir.
        audio = recog.listen(audio_file)
        print('Sesler Yazıya Çevriliyor...')
        # Satırı, alınan ses kaydını Google'ın ses tanıma API'sini kullanarak metin formatına çevirir.
        print(recog.recognize_google(audio, language='tr-TR') + ' dediniz.')
"""



def speechlan(lang):
    mic = sr.Microphone()
    recog = sr.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        try:
            audio = recog.listen(audio_file, timeout=5)  # Maksimum 5 saniye bekle
            return recog.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            return "Anlaşılamadı, lütfen tekrar deneyin."
        except sr.RequestError:
            return "Bağlantı hatası, lütfen internetinizi kontrol edin."


