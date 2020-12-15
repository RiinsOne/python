# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
    
#     trs = soup.find('div', {'data-mutable-id': 'Block_3'}).find('div', class_='market-inline-block-table-wrapper').find('table', class_='td-border table-layout-fixed').find_all('tr')
    
#     data = []
    
#     for tr in trs[1:-2]:
#         data_pairs = []
        
#         tds_under = tr.find_all('td', {'data-sel': re.compile('Меньше')})
#         for td in tds_under:  
#             p_under = 'Тотал меньше {}'
#             p_under_name = td.find('div', class_='coeff-handicap').text.strip()
#             name_under = p_under.format(p_under_name)
#             rate_under = td.find('span').text.strip()
#             data_pairs.append(
#                 (name_under, float(rate_under))
#             )
        
#         tds_over = tr.find_all('td', {'data-sel': re.compile('Больше')})
#         for td in tds_over:
#             p_over = 'Тотал больше {}'
#             p_over_name = td.find('div', class_='coeff-handicap').text.strip()
#             name_over = p_over.format(p_over_name)
#             rate_over = td.find('span').text.strip()
            
#             data_pairs.append(
#                 (name_over, float(rate_over))
#             )

#         data.append(data_pairs)
    
#     for i in data:
#         print(i)

