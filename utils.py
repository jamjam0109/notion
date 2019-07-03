def date_form(date):
    year = date.split('-')[0]
    month = date.split('-')[1]
    month = month.lower()
    day = date.split('-')[2]

    if len(month) == 1:
        month = '0' + month

    if len(day) == 1:
        day = '0' + day

    if month == 'january' or month == 'jan':
        month = '01'
    elif month == 'february' or month == 'feb':
        month = '02'
    elif month == 'march' or month == 'mar':
        month = '03'
    elif month == 'april' or month == 'apr':
        month = '04'
    elif month == 'may':
        month = '05'
    elif month == 'june' or month == 'jun':
        month = '06'
    elif month == 'july' or month == 'jul':
        month = '07'
    elif month == 'august' or month == 'aug':
        month = '08'
    elif month == 'september' or month == 'sep':
        month = '09'
    elif month == 'october' or month == 'oct':
        month = '10'
    elif month == 'november' or month == 'nov':
        month = '11'
    elif month == 'december' or month == 'dec':
        month = '12'

    output = year + '-' + month + '-' + day

    return output


def create_output(title, date, url):
    output = list()

    output.append(title)
    output.append(date)
    output.append(url)

    return output