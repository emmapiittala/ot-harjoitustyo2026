import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassansaldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
    
    def test_edulliset_oikein_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_rahanmaara_kasvaa_edullisen_lounaan_hinnalla_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        
    def test_rahanmaara_kasvaa_maukkaan_lounaan_hinnalla_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_vaihtoraha_oikein_edullisen_lounaan_hinnalla(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
           
    def test_vaihtoraha_oikein_maukkaan_lounaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        
    def test_rahanmaara_ei_riita_edullisen_lounaan_ostamiseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
                   
    def test_rahanmaara_ei_riita_maukkaan_lounaan_ostamiseen(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edulliset_kpl_maara_ei_kasva_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaasti_kpl_maara_ei_kasva_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_edulliset_kpl_maara_kasvaa_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_maukkaasti_kpl_maara_kasvaa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        
    def test_jos_kortilla_rahaa_edullissti_ostamiseen_true(self):
        kortti = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(kortti,True)

    def test_jos_kortilla_rahaa_maukkaasti_ostamiseen_true(self):
        kortti = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(kortti,True)
        
    def test_jos_kortilla_ei_ole_rahaa_edullisen_ostamiseen_false(self):
        self.maksukortti.ota_rahaa(1000)
        kortti = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(kortti,False)

    def test_jos_kortilla_ei_ole_rahaa_maukkaasti_ostamiseen_false(self):
        self.maksukortti.ota_rahaa(1000)
        kortti = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(kortti,False)
        
    def test_edullisestti_kpl_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaasti_kpl_maara_kasvaa_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_saldo_vahenee_oikein_jos_rahaa_on(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.00)
    
    def test_saldo_ei_muutu_jos_rahaa_ei_ole_riittavasti(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        
    def test_edulliset_kpl_maara_ei_kasva_jos_raha_ei_riita_kortilla(self):
        self.maksukortti.ota_rahaa(239)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaasti_kpl_maara_ei_kasva_jos_raha_ei_riita_kortilla(self):
        self.maksukortti.ota_rahaa(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kassan_raha_oikein_korttimaksulla_edullisen_lounaan_hinnalla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassan_raha_oikein_korttimaksulla_maukkaan_lounaan_hinnalla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
        
    def test_neg_rahan_lataaminen_ei_kasvata_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-2500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
    
    def test_neg_rahan_lataaminen_ei_muuta_kassansaldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-2500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_rahan_lataaminen_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102500)