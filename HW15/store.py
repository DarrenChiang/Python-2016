import stafflib as stf

stf.addStaff("John", "Smith", 43, "11-Nov-2008", "janitor", 645, 1000)
stf.addStaff("Bob", "Johnson", 25, "24-Sep-2013", "janitor", 30, 200)

stf.showRegistre()

stf.addDay()

stf.showRegistre()

stf.deleteStaff("Bob", "Johnson")

stf.showRegistre()
