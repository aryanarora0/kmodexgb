import pandas as pd

def load_data(filepath, ryear1, ryear2):
    try:
        df = pd.read_csv(filepath)
        df = df[df['Year'].isin([int(ryear1), int(ryear2)])]
        return df
    except FileNotFoundError:
        raise Exception("Not found")
    except Exception as e:
        raise Exception(str(e))
    
def map_columns(df):
    mappings = {
        'Education': {
            1.0 : '8th grade or less',
            2.0 : '9 - 12th grade, no diploma',
            3.0 : 'High school graduate or GED completed',
            4.0 : 'Some college credit, but no degree',
            5.0 : 'Associate degree',
            6.0 : 'Bachelors degree',
            7.0 : 'Masters degree',
            8.0 : 'Doctorate or professional degree',
            9.0 : 'Unknown'
        },
        'Month of Death': {
            1 : 'January',
            2 : 'February',
            3 : 'March',
            4 : 'April',
            5 : 'May',
            6 : 'June',
            7 : 'July',
            8 : 'August',
            9 : 'September',
            10 : 'October',
            11 : 'November',
            12 : 'December'
        },
        'AgeCategory': {
            23: '1 year',
            24: '2 years',
            25: '3 years',
            26: '4 years',
            27: '5 - 9 years',
            28: '10 - 14 years',
            29: '15 - 19 years',
            30: '20 - 24 years',
            31: '25 - 29 years',
            32: '30 - 34 years',
            33: '35 - 39 years',
            34: '40 - 44 years',
            35: '45 - 49 years',
            36: '50 - 54 years',
            37: '55 - 59 years',
            38: '60 - 64 years',
            39: '65 - 69 years',
            40: '70 - 74 years',
            41: '75 - 79 years',
            42: '80 - 84 years',
            43: '85 - 89 years',
            44: '90 - 94 years',
            45: '95 - 99 years',
            46: '100 - 104 years',
            47: '105 - 109 years'
        },
        'Marital Status': {
            'S':'Never married, single',
            'M':'Married',
            'W':'Widowed',
            'D':'Divorced',
            'U':'Marital Status unknown'
        },
        'Manner of Death': {
            1.0: 'Accident',
            2.0: 'Suicide',
            3.0: 'Homicide',
            4.0: 'Pending investigation',
            5.0: 'Could not determine',
            6.0: 'Self-Inflicted',
            7.0: 'Natural'
        },
        'Race': {
            1: 'White',
            2: 'Black',
            3: 'American Indian or Alaskan Native (AIAN)',
            4: 'Asian Indian',
            5: 'Chinese',
            6: 'Filipino',
            7: 'Japanese',
            8: 'Korean',
            9: 'Vietnamese',
            10: 'Other or Multiple Asian',
            11: 'Hawaiian',
            12: 'Guamanian',
            13: 'Samoan',
            14: 'Other or Multiple Pacific Islander',
            15: 'Black and White',
            16: 'Black and AIAN',
            17: 'Black and Asian',
            18: 'Black and Native Hawaiian or Other Pacific Islander (NHOPI)',
            19: 'AIAN and White',
            20: 'AIAN and Asian',
            21: 'AIAN and NHOPI',
            22: 'Asian and White',
            23: 'Asian and NHOPI',
            24: 'NHOPI and White',
            25: 'Black, AIAN and White',
            26: 'Black, AIAN and Asian',
            27: 'Black, AIAN and NHOPI',
            28: 'Black, Asian and White',
            29: 'Black, Asian and NHOPI',
            30: 'Black, NHOPI and White',
            31: 'AIAN, Asian and White',
            32: 'AIAN, NHOPI and White',
            33: 'AIAN, Asian and NHOPI',
            34: 'Asian, NHOPI and White',
            35: 'Black, AIAN, Asian and White',
            36: 'Black, AIAN, Asian and NHOPI',
            37: 'Black, AIAN, NHOPI and White',
            38: 'Black, Asian, NHOPI and White',
            39: 'AIAN, Asian, NHOPI and White',
            40: 'Black, AIAN, Asian, NHOPI and White'
        },
        'Occupation': {
            1.0: 'Management Occupations',
            2.0: 'Business & Financial Operations Occupations',
            3.0: 'Computer & Mathematical Occupations',
            4.0: 'Architecture & Engineering Occupations',
            5.0: 'Life, Physical, & Social Science Occupations',
            6.0: 'Community & Social Services Occupations',
            7.0: 'Legal Occupations',
            8.0: 'Education, Training, & Library Occupations',
            9.0: 'Arts, Design, Entertainment, Sports, & Media Occupations',
            10.0: 'Healthcare Practitioners & Technical Occupations',
            11.0: 'Healthcare Support Occupations',
            12.0: 'Protective Service Occupations',
            13.0: 'Food Preparation & Serving Related Occupations',
            14.0: 'Building & Grounds Cleaning & Maintenance Occupations',
            15.0: 'Personal Care & Service Occupations',
            16.0: 'Sales & Related Occupations',
            17.0: 'Office & Administrative Support Occupations',
            18.0: 'Farming, Fishing, & Forestry Occupations',
            19.0: 'Construction & Extraction Occupations',
            20.0: 'Installation, Maintenance, & Repair Occupations',
            21.0: 'Production Occupations',
            22.0: 'Transportation & Material Moving Occupations',
            24.0: 'Military',
            25.0: 'Other, Misc (exc Housewife)',
            26.0: 'Other, Housewife'
        },
        'Death': {
            420:'Accidental Drug Poisoning',
            425:'Suicide Drug Poisoning',
            443:'Undetermined Drug Poisoning'
        }
    }
    for column, mapping in mappings.items():
        df[column] = df[column].map(mapping)
    return df

def main():
    df = load_data('T404.csv', 2020, 2021)
    df = map_columns(df)
    df.to_csv('Updated.csv', index=False)

if __name__ == '__main__':
    main()

    