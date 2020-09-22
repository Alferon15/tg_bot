from ..models import ServiceCode


def load_data_from_file():
    f = open('/home/Alferon15/alferon15.pythonanywhere.com/osk_database/services/data.csv', 'r', encoding='utf-8')
    f.readline()
    n = 30
    for row in f:
        if n < 1:
            break
        spl = row.split(sep='#')

        try:
            sc = ServiceCode.objects.get(service_code=spl[0])
        except ServiceCode.DoesNotExist:
            sc = None

        if not sc:
            sc = ServiceCode.objects.create(
                service_code=spl[0],
                status=spl[1],
                org_owner=spl[3],
                object_type=spl[6],
                address=spl[7],
                responsible=spl[8],
                name_pc=spl[9],
                level=spl[11],
                model=spl[12],
                category=spl[13],
                sn=spl[15],
                ais_tp=spl[19],
            )

    res = 'Ok'
    return res
