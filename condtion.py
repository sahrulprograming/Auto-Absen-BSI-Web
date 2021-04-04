def matkul():
    import json
    import datetime
    data = json.load(open('link_matkul.json'))
    x = datetime.datetime.now()
    sekarang = x.strftime("%w")
    jam = x.strftime("%H:%M")
    if sekarang == '1':
        if jam >= '11:40' and jam < '14:10':
            ket = "Hari Senin"
            matkul_sekarang = data['senin1']
        elif jam >= '14:10' and jam < '16:40':
            ket = "Hari Senin"
            matkul_sekarang = data['senin2']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    elif sekarang == '2':
        if jam >= '09:10' and jam < '10:50':
            ket = "Hari Selasa"
            matkul_sekarang = data['selasa1']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    elif sekarang == '3':
        if jam >= '07:30' and jam < '10:00':
            ket = "Hari Rabu"
            matkul_sekarang = data['rabu1']
        else:
            ket ="Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0

    elif sekarang == '5':
        if jam >= '09:10' and jam < '11:40':
            ket = "hari Jum'At"
            matkul_sekarang = data['jumat1']
        elif jam >= '13:20' and jam < '16:40':
            ket = "hari Jum'At"
            matkul_sekarang = data['jumat2']
        else:
            ket = "Jadwal Pelajaran Belum Mulai atau sudah Selesai"
            matkul_sekarang = 0
    else:
        ket ='Hari Libur'
        matkul_sekarang = 0

    return ket, matkul_sekarang