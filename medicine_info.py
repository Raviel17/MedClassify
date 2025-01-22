# Baca kelas obat dari file
with open('model/class_names.txt', 'r') as f:
    class_names = f.read().splitlines()

# Buat template informasi obat
MEDICINE_INFO = {}
for class_name in class_names:
    MEDICINE_INFO[class_name.lower()] = {
        "nama": class_name,
        "dosis": "Sesuai petunjuk dokter",
        "deskripsi": f"Informasi detail untuk {class_name}",
        "efek_samping": "Konsultasikan dengan dokter"
    }

# Update informasi spesifik untuk setiap obat
MEDICINE_INFO.update({
    "alpara": {
        "nama": "Alpara",
        "dosis": "1 tablet, 3 kali sehari",
        "deskripsi": "Obat untuk mengatasi gejala alergi seperti bersin-bersin, gatal-gatal, dan hidung tersumbat",
        "efek_samping": "Mengantuk, mulut kering, gangguan penglihatan"
    },
    "amoxicillin": {
        "nama": "Amoxicillin",
        "dosis": "500mg, 3 kali sehari",
        "deskripsi": "Antibiotik untuk mengobati berbagai infeksi bakteri pada saluran pernapasan, telinga, sinus, dan saluran kemih",
        "efek_samping": "Mual, diare, ruam kulit, gangguan pencernaan"
    },
    "panadol": {
        "nama": "Panadol",
        "dosis": "500mg-1000mg setiap 4-6 jam (maksimal 4000mg per hari)",
        "deskripsi": "Obat untuk meredakan nyeri ringan hingga sedang seperti sakit kepala, sakit gigi, nyeri otot, dan menurunkan demam",
        "efek_samping": "Mual, gangguan fungsi hati jika dosis berlebihan"
    },
    "promag": {
        "nama": "Promag",
        "dosis": "1-2 tablet, 3-4 kali sehari",
        "deskripsi": "Obat untuk mengatasi gejala sakit maag, kembung, dan nyeri lambung dengan menetralisir asam lambung berlebih",
        "efek_samping": "Konstipasi, diare, mual, sakit kepala"
    },
    "sanmol": {
        "nama": "Sanmol",
        "dosis": "500mg-1000mg setiap 4-6 jam (maksimal 4000mg per hari)",
        "deskripsi": "Obat pereda nyeri dan penurun demam yang mengandung paracetamol, aman untuk anak-anak dan dewasa",
        "efek_samping": "Mual, ruam kulit, gangguan fungsi hati jika overdosis"
    },
    "decolgen": {
        "nama": "Decolgen",
        "dosis": "1 tablet setiap 6-8 jam",
        "deskripsi": "Obat flu yang mengandung kombinasi paracetamol, phenylephrine HCl, dan chlorpheniramine maleate untuk meredakan gejala flu",
        "efek_samping": "Mengantuk, mulut kering, pusing, gangguan penglihatan"
    },
    "bodrex": {
        "nama": "Bodrex",
        "dosis": "1 tablet setiap 6 jam",
        "deskripsi": "Obat pereda nyeri dan demam yang mengandung paracetamol dan caffeine untuk sakit kepala dan nyeri ringan",
        "efek_samping": "Sulit tidur, jantung berdebar, mual"
    },
    "insto": {
        "nama": "Insto",
        "dosis": "1-2 tetes pada setiap mata, 3-4 kali sehari",
        "deskripsi": "Tetes mata untuk meredakan iritasi, kemerahan, dan kelelahan mata",
        "efek_samping": "Perih sementara, pandangan kabur setelah penggunaan"
    },
    "paramex": {
        "nama": "Paramex",
        "dosis": "1 tablet setiap 6 jam",
        "deskripsi": "Obat sakit kepala yang mengandung paracetamol, caffeine, dan propyphenazone",
        "efek_samping": "Mengantuk, mual, gangguan pencernaan"
    },
    "mixagrip": {
        "nama": "Mixagrip",
        "dosis": "1 tablet setiap 8 jam",
        "deskripsi": "Obat flu yang mengandung paracetamol, phenylephrine HCl, dan dextromethorphan HBr",
        "efek_samping": "Mengantuk, mulut kering, pusing"
    },
    "neuralgin": {
        "nama": "Neuralgin",
        "dosis": "1 tablet, 3 kali sehari",
        "deskripsi": "Obat untuk meredakan nyeri saraf, sakit kepala, dan nyeri otot",
        "efek_samping": "Mengantuk, pusing, gangguan pencernaan"
    },
    "ultraflu": {
        "nama": "Ultraflu",
        "dosis": "1 tablet setiap 8 jam",
        "deskripsi": "Obat flu yang mengandung paracetamol, phenylephrine, dan chlorpheniramine untuk meredakan gejala flu seperti demam, hidung tersumbat, dan bersin",
        "efek_samping": "Mengantuk, mulut kering, pusing, gangguan penglihatan"
    },
    "oskadon": {
        "nama": "Oskadon",
        "dosis": "1 tablet setiap 6 jam",
        "deskripsi": "Obat analgesik dan antipiretik yang mengandung paracetamol, caffeine, dan propyphenazone untuk meredakan sakit kepala dan nyeri",
        "efek_samping": "Mual, gangguan pencernaan, jantung berdebar"
    },
    "komix": {
        "nama": "Komix",
        "dosis": "1 sachet setiap 8 jam",
        "deskripsi": "Obat batuk dalam bentuk sirup sachet yang mengandung dextromethorphan HBr untuk meredakan batuk tidak berdahak",
        "efek_samping": "Mengantuk, pusing, mual"
    },
    "konidin": {
        "nama": "Konidin",
        "dosis": "1 tablet setiap 8 jam",
        "deskripsi": "Obat batuk yang mengandung dextromethorphan HBr dan chlorpheniramine maleate untuk meredakan batuk dan gejala flu",
        "efek_samping": "Mengantuk, mulut kering, gangguan penglihatan"
    },
    "paracetamol": {
        "nama": "Paracetamol",
        "dosis": "500mg-1000mg setiap 4-6 jam (maksimal 4000mg per hari)",
        "deskripsi": "Obat analgesik dan antipiretik untuk meredakan nyeri ringan hingga sedang dan menurunkan demam",
        "efek_samping": "Mual, ruam kulit, gangguan fungsi hati jika overdosis"
    },
    "ibuprofen": {
        "nama": "Ibuprofen",
        "dosis": "200-400mg setiap 4-6 jam (maksimal 1200mg per hari)",
        "deskripsi": "Obat antiinflamasi non-steroid (NSAID) untuk meredakan nyeri, demam, dan peradangan",
        "efek_samping": "Sakit perut, mual, gangguan pencernaan, meningkatkan risiko pendarahan"
    },
    "antangin": {
        "nama": "Antangin",
        "dosis": "1 sachet atau 1-2 tablet, 3 kali sehari",
        "deskripsi": "Obat herbal untuk meredakan masuk angin, mual, kembung, dan gejala flu",
        "efek_samping": "Umumnya aman, namun dapat menyebabkan mengantuk pada beberapa orang"
    },
    "tolak-angin": {
        "nama": "Tolak Angin",
        "dosis": "1 sachet, 3 kali sehari",
        "deskripsi": "Obat herbal untuk mengatasi masuk angin, flu, dan menjaga daya tahan tubuh",
        "efek_samping": "Jarang terjadi, bisa menyebabkan mengantuk pada beberapa orang"
    },
    "betadine": {
        "nama": "Betadine",
        "dosis": "Oleskan pada area yang diperlukan, 2-3 kali sehari",
        "deskripsi": "Antiseptik yang mengandung povidone iodine untuk membersihkan dan mencegah infeksi pada luka ringan",
        "efek_samping": "Iritasi kulit, gatal, kemerahan"
    },
    "vicks-vaporub": {
        "nama": "Vicks VapoRub",
        "dosis": "Oleskan secukupnya pada dada dan leher sebelum tidur",
        "deskripsi": "Obat oles untuk meredakan gejala flu seperti hidung tersumbat dan batuk",
        "efek_samping": "Iritasi kulit, sensasi terbakar ringan"
    },
    "diapet": {
        "nama": "Diapet",
        "dosis": "2 tablet, 3-4 kali sehari",
        "deskripsi": "Obat herbal untuk mengatasi diare, mual, dan gangguan pencernaan dengan kandungan daun jambu biji dan kunyit",
        "efek_samping": "Jarang terjadi, bisa menyebabkan konstipasi ringan"
    },
    "dumin_paracetamol": {
        "nama": "Dumin Paracetamol",
        "dosis": "500mg-1000mg setiap 4-6 jam (maksimal 4000mg per hari)",
        "deskripsi": "Obat analgesik dan antipiretik untuk meredakan nyeri dan menurunkan demam",
        "efek_samping": "Mual, ruam kulit, gangguan fungsi hati jika overdosis"
    },
    "laxing": {
        "nama": "Laxing",
        "dosis": "1-2 tablet sebelum tidur",
        "deskripsi": "Obat pencahar untuk mengatasi sembelit dengan cara melunakkan feses",
        "efek_samping": "Kram perut, mual, diare jika dosis berlebihan"
    },
    "panadol_anak": {
        "nama": "Panadol Anak",
        "dosis": "Sesuai usia dan berat badan anak (lihat kemasan)",
        "deskripsi": "Obat penurun demam dan pereda nyeri khusus untuk anak-anak, dengan rasa yang lebih enak",
        "efek_samping": "Mual, ruam kulit, gangguan fungsi hati jika overdosis"
    },
    "panadol_extra": {
        "nama": "Panadol Extra",
        "dosis": "1-2 tablet setiap 4-6 jam (maksimal 8 tablet per hari)",
        "deskripsi": "Kombinasi paracetamol dan kafein untuk meredakan nyeri kepala, gigi, dan otot dengan efek lebih kuat",
        "efek_samping": "Sulit tidur, jantung berdebar, mual, gangguan fungsi hati jika berlebihan"
    },
    "paramex_sk": {
        "nama": "Paramex SK",
        "dosis": "1 tablet setiap 6 jam",
        "deskripsi": "Obat sakit kepala dengan formula khusus yang mengandung paracetamol, caffeine, dan propyphenazone",
        "efek_samping": "Mengantuk, mual, gangguan pencernaan"
    },
    "procold_flu": {
        "nama": "Procold Flu",
        "dosis": "1 tablet setiap 8 jam",
        "deskripsi": "Obat flu yang mengandung paracetamol, phenylephrine HCl, dan chlorpheniramine maleate untuk meredakan gejala flu",
        "efek_samping": "Mengantuk, mulut kering, pusing"
    },
    "sumagesic_paracetamol": {
        "nama": "Sumagesic Paracetamol",
        "dosis": "500mg-1000mg setiap 4-6 jam (maksimal 4000mg per hari)",
        "deskripsi": "Obat analgesik dan antipiretik untuk meredakan nyeri dan menurunkan demam",
        "efek_samping": "Mual, ruam kulit, gangguan fungsi hati jika overdosis"
    }
}) 

# Tambahkan fungsi rekomendasi berdasarkan confidence
def get_recommendation(confidence_level):
    """
    Memberikan rekomendasi berdasarkan tingkat kepercayaan prediksi
    Args:
        confidence_level: float antara 0-1
    Returns:
        dict: Rekomendasi dan tindakan yang disarankan
    """
    if confidence_level >= 0.95:
        return {
            "status": "Sangat Akurat",
            "message": "Prediksi sangat akurat. Informasi obat dapat diandalkan.",
            "tindakan": "Ikuti petunjuk penggunaan sesuai informasi yang diberikan.",
            "warna": "green"
        }
    elif confidence_level >= 0.85:
        return {
            "status": "Akurat",
            "message": "Prediksi cukup akurat. Informasi obat dapat dipercaya.",
            "tindakan": "Periksa kembali nama obat pada kemasan untuk memastikan.",
            "warna": "blue"
        }
    elif confidence_level >= 0.70:
        return {
            "status": "Cukup Akurat",
            "message": "Prediksi memiliki tingkat kepercayaan sedang.",
            "tindakan": "Disarankan untuk memverifikasi dengan membaca label obat.",
            "warna": "orange"
        }
    else:
        return {
            "status": "Kurang Akurat",
            "message": "Tingkat kepercayaan prediksi rendah.",
            "tindakan": "Harap periksa kembali dengan foto yang lebih jelas atau konsultasikan dengan apoteker.",
            "warna": "red"
        }

# Update template informasi obat
class MedicineInfo:
    def __init__(self, medicine_info, confidence=None):
        self.info = medicine_info
        self.confidence = confidence
        self.recommendation = get_recommendation(confidence) if confidence else None

    def get_complete_info(self):
        """Mengembalikan informasi lengkap termasuk rekomendasi"""
        result = self.info.copy()
        if self.recommendation:
            result.update({
                "confidence_info": self.recommendation
            })
        return result

# Update di app.py untuk menggunakan fitur baru
def get_medicine_info(predicted_class, confidence):
    base_info = MEDICINE_INFO.get(predicted_class.lower(), {})
    medicine_info = MedicineInfo(base_info, confidence)
    return medicine_info.get_complete_info() 