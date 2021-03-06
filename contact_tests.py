# from cgi import test
import unittest
import pyperclip
from contact import Contact
class testclass (unittest.TestCase) :


    def setUp(self):

     self.new_contact = Contact("Brian", "otieno", "077777777","b@gmail.com")

    def test_init (self):
        self.assertEqual(self.new_contact.first_name,"Brian")
        self.assertEqual(self.new_contact.last_name,"otieno")
        self.assertEqual(self.new_contact.phone_number,"077777777")
        self.assertEqual(self.new_contact.email,"b@gmail.com")
        
        
    def test_save_contact(self):
     self.new_contact.save_contact()
     self.assertEqual(len(Contact.contact_list),1)

    def tearDown(self):
      Contact.contact_list = []


    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("kenya","republic","077777","k@10.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact= Contact("knya","republic","077777","k@10.com")
        test_contact.save_contact()
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("rwanda","democrat","017777","r@.com")
        test_contact.save_contact()

        found_contact = Contact.find_by_number("017777")
        self.assertEqual(found_contact.phone_number,test_contact.phone_number)

    def test_contact_exists(self):
        self.new_contact.save_contact()
        test_contact = Contact("ken","ok","08888","c@ken")
        test_contact.save_contact()

        contact_exists = Contact.contact_exists("08888")
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(),Contact.contact_list)


    # def test_copy_email(self):
    #     self.new_contact.save_contact()
    #     Contact.copy_email("08888")
    #     self.assertEqual(self.new_contact.email,pyperclip.paste())

    # def test_copy_email(self):
    #     self.new_contact.save_contact()
    #     Contact.copy_email("b@gmail.com")
    #     self.assertEqual(self.new_contact.email,pyperclip.paste())




if __name__=="__main__":
    unittest.main()

    
        

  
