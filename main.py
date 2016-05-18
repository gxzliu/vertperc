# *******************************************************
# vertperc 
# george liu
# main method
# date: 4.3.16
# *******************************************************


import percolation as perc

def main():
    site_matrix=perc.make_matrix(30,0.6)
    perc.write_file('sites.txt',site_matrix)
    sites_read=perc.read_file('sites.txt')
    sites_flow=perc.vert_flow(sites_read)
    if perc.percolate(sites_flow):
        print('percolates')
    else:
        print('does not percolate')
    
main()