import pytest
import time
import datetime
from Pages import LoginPage, PatientSearchPage, AddPatient, PatientHistory, AlgoPages, AppointmentResults, \
    BookAppointment, AppointmentDetails
from TestData import Constants


@pytest.mark.usefixtures("setup")
class Test_001:

    @pytest.mark.sanity
    def test_login(self, setup):
        self.username = "yash.chindalia@rsystems.com"
        self.password = "Zero!@34"

        self._driver = setup
        self.lp = LoginPage.Login(self._driver)

        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        time.sleep(5)

    # @pytest.mark.sanity
    def test_PatientSearch(self, setup):
        self._driver = setup

        self.psp = PatientSearchPage.PatientSearch(self._driver)
        self.psp.enter_Fname(Constants.FIRST_NAME)
        self.psp.enter_Lname(Constants.LAST_NAME)
        self.psp.enter_Date(Constants.DOB)
        self.psp.click_SearchPatient()
        time.sleep(5)
        self.psp.click_Create()
        time.sleep(5)

    @pytest.mark.sanity
    def test_PatientSearch_memberID(self, setup):
        self._driver = setup

        self.psp = PatientSearchPage.PatientSearch(self._driver)
        self.psp.enter_Member("off001")
        self.psp.click_SearchPatient()
        time.sleep(5)
        self.psp.click_Book()
        time.sleep(5)

    # @pytest.mark.sanity
    def test_AddPatient(self, setup):
        self._driver = setup

        self.AP = AddPatient.AddPatient(self._driver)

        self.AP.enter_Member(Constants.MEMBER_ID)
        self.AP.enter_Fname(Constants.FIRST_NAME)
        self.AP.enter_Lname(Constants.LAST_NAME)
        self.AP.enter_Date(Constants.DOB)
        self.AP.select_Gender(Constants.GENDER)
        self.AP.enter_HPhone(Constants.HOME_PHONE)
        self.AP.enter_MPhone(Constants.MOBILE_PHONE)
        self.AP.enter_Address1(Constants.ADDRESS_1)
        self.AP.enter_City(Constants.CITY)
        self.AP.select_State(Constants.STATE)
        self.AP.enter_Zip(Constants.ZIP)
        self.AP.enter_Email(Constants.EMAIL)
        self.AP.click_Save("test")

        time.sleep(5)

    # @pytest.mark.sanity
    def test_PatientHistory(self, setup):
        self._driver = setup

        self.PH = PatientHistory.PatientHistory(self._driver)
        self.PH.click_Book()

    @pytest.mark.sanity
    @pytest.mark.parametrize("bookingDate",
                             [(datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%m/%d/%Y")])
    def test_AppointmentSearch(self, setup, bookingDate):
        self._driver = setup

        self.Alp = AlgoPages.AlgoPages(self._driver)
        self.AR = AppointmentResults.AppointmentResults(self._driver)

        self.Alp.select_Specialty("Internal Medicine")
        self.Alp.enter_bookingDate(bookingDate)
        self.Alp.click_first_Next()
        time.sleep(3)
        self.Alp.enter_DOB(Constants.DOB)
        self.Alp.click_next()
        time.sleep(3)
        self.Alp.select_PatientType("New")
        self.Alp.select_preferredProvider("No preference")
        self.Alp.click_next()
        time.sleep(3)
        self.Alp.select_preferredLocation("No preference")
        self.Alp.click_next()
        time.sleep(10)

        self.AR.click_book()
        time.sleep(10)

    @pytest.mark.sanity
    def test_BookAppointment(self, setup):
        self._driver = setup

        self.BA = BookAppointment.BookAppointment(self._driver)
        self.AD = AppointmentDetails.AppointmentDetails(self._driver)

        self.BA.enter_reason("This is for Automation")
        self.BA.enter_custom("55")
        self.BA.enter_referringProvider("NA")
        self.BA.click_scheduleAppointment()
        time.sleep(1)
        self.BA.click_custom1()
        self.BA.click_custom()
        time.sleep(10)

        assert self.AD.get_AD_test() == "Appointment Details"
        self._driver.save_screenshot(".\\Screenshots\\auto.png")
