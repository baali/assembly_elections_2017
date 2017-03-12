import csv
import pandas

# Numbers are based on 2012 turnout
electors = [line for line in csv.DictReader(open('electors.csv', 'r'))]

demography_religion = {}
states = ['up', 'goa', 'punjab', 'uttarakhand', 'manipur']
for state in states:
    # demography = pandas.read_csv('Demographic-%s.csv' %state, header=[0, 1])
    assembly = pandas.read_csv('%s.csv' %state, header=[0, 1])
    for ac in assembly['Name of AC', 'Unnamed: 1_level_1']:
        results_2017 = assembly[assembly['Name of AC', 'Unnamed: 1_level_1'] == ac]
        names = results_2017[[value for value in results_2017.columns.values if value[1] == 'Candidate Name']].values
        votes = results_2017[[value for value in results_2017.columns.values if value[1] == 'Party Votes']].values
        nota = results_2017[[value for value in results_2017.columns.values if value[0] == 'NOTA Votes']].values[0, 0]
        winning_margin = results_2017[[value for value in results_2017.columns.values if value[0] == 'Winning Margin of Votes']].values[0, 0]
        winner_party = results_2017[[value for value in results_2017.columns.values if value[0] == 'Winner']].values[0, 0]
        if nota > winning_margin:
            print('{}:{} - Winning party: {}, Nota:{}, Winning Margin:{}'.format(state, ac, winner_party, nota, winning_margin))

        row = demography[demography[' AC ', 'Unnamed: 1_level_1'] == ac]
        ac = ac.strip().lower()
        if ac == 'gaziabad':
            ac = 'ghaziabad'
        numbers_ac = [electoral for electoral in electors if electoral['AC_NAME'].strip().lower() in ac][0]
        # print(ac, numbers_ac['TOT_VOTERS'], )
        voters = numbers_ac['TOT_VOTERS']
        muslims = int(row[[value for value in row if value[1] == 'Muslim Range']].values[0,0].split('-')[0])
        try:
            christians = int(row[[value for value in row if value[1] == 'Christian Range']].values[0,0].split('-')[0])
        except IndexError:
            christians = 0
        try:
            sc = row[[value for value in row if value[1] == 'SC%']].values[0, 0]*int(numbers_ac['TOT_VOTERS'])/100
            if row[[value for value in row if value[1] == 'SC%']].values[0, 0] > 20 and winner_party == 'BJP':
                print ('SC more than 20%({}) but BJP won in {}'.format('%.2f' %row[[value for value in row if value[1] == 'SC%']].values[0, 0], ac))
        except IndexError:
            sc = 0
        try:
            st = row[[value for value in row if value[1] == 'ST%']].values[0, 0]*int(numbers_ac['TOT_VOTERS'])/100
        except IndexError:
            st = 0
        hindus = int(row[[value for value in row if value[1] == 'Hindu Range']].values[0,0].split('-')[0])
        if muslims > 30 and winner_party == 'BJP':
            print ('Muslims more than 30%({}) but BJP won in {}'.format(muslims, ac))
            
        # print('{}:{}, {} won, hindus: {}, muslims: {}, christians: {}, sc: {}, st: {}'.format(ac, state, winner_party, hindus, muslims, christians, '%.2f'%sc, '%.2f'%st))
        # List constituencies where NOTA was within 50% of winner margin.
        # List parties which are going below NOTA
