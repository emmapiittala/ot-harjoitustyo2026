import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        
    def test_alkusaldo_oikeiin(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
        
    def test_saldo_vahenee_oikein_jos_rahaa_on(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_riittavasti(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_true_jos_rahat_riittaa(self):
        saldo = self.maksukortti.ota_rahaa(500)
        self.assertEqual(saldo,True)
        
    def test_false_jos_rahat_ei_riiita(self):
        saldo = self.maksukortti.ota_rahaa(10000)
        self.assertEqual(saldo, False)
        