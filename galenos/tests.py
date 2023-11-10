from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestGalenos(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    print("Ejecutando pruebas...")
    def test_g01(self):
        print("TestG01")
        self.selenium.get("http://localhost:8000/index/")
        time.sleep(2)
        self.selenium.maximize_window()
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)

    def test_g02(self):
        print("TestG02")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_username").send_keys("fespinoza")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("fabo1234")
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Usuario ha iniciado sesión satisfactoriamente"
        alert.accept()
        time.sleep(1)
        self.selenium.get("http://localhost:8000/galenoslogin/indexwithlogin")
        time.sleep(3)

    def test_g03(self):
        print("TestG03")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_username").send_keys("fespinoza")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("1234")
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Campos erróneos, por favor corrija la información"
        alert.accept()
        time.sleep(1)

        
    def test_g04(self):
        print("TestG04")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_username").send_keys("noza")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("fabo1234")
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Campos erróneos, por favor corrija la información"
        alert.accept()
        time.sleep(1)

    def test_g05(self):
        print("TestG05")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(3)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Campos vacíos, por favor ingresar información"
        alert.accept()
        time.sleep(1)

    def test_g06(self):
        print("TestG06")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").send_keys("FespinoZa")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("FabO1234")
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(3)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Campos erróneos, por favor corrija la información"
        alert.accept()
        time.sleep(1)

    def test_g07(self):
        print("TestG07")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(4) > .nav-link").click()
        time.sleep(2)
        self.selenium.find_element(By.ID, "id_username").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_username").send_keys("fespinoza")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_password").send_keys("fabo1234")
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)
        alert = self.selenium.switch_to.alert
        assert alert.text == "Usuario ha iniciado sesión satisfactoriamente"
        alert.accept()
        time.sleep(1)
        self.selenium.get("http://localhost:8000/galenoslogin/indexwithlogin")
        time.sleep(3)
        self.selenium.find_element(By.LINK_TEXT, "Reservar cita").click()
        time.sleep(3)
        self.selenium.find_element(By.ID, "id_rut").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_rut").send_keys("123456789")
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_sucursal").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_sucursal")
        dropdown.find_element(By.XPATH, "//option[. = 'Viña del Mar']").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_prevision").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_prevision")
        dropdown.find_element(By.XPATH, "//option[. = 'Colmena Golden Cross']").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_especialidad").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_especialidad")
        dropdown.find_element(By.XPATH, "//option[. = 'Ortodoncia Invisible']").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_fecha_month").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_fecha_month")
        dropdown.find_element(By.XPATH, "//option[. = 'May']").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_fecha_day").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_fecha_day")
        dropdown.find_element(By.XPATH, "//option[. = '14']").click()
        time.sleep(1)
        self.selenium.find_element(By.ID, "id_fecha_year").click()
        time.sleep(1)
        dropdown = self.selenium.find_element(By.ID, "id_fecha_year")
        dropdown.find_element(By.XPATH, "//option[. = '2024']").click()
        time.sleep(1)
        self.selenium.find_element(By.CSS_SELECTOR, "button:nth-child(7)").click()
        time.sleep(1)
        self.selenium.find_element(By.LINK_TEXT, "Volver al menú principal").click()
        time.sleep(1)

        print("Pruebas finalizadas")

    def test_g08(self):
        print("TestG08")
        self.selenium.get("http://localhost:8000/index/")
        self.selenium.maximize_window()
        time.sleep(2)
        