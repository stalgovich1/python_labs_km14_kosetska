#я не дуже зрозуміла декоратори(((
while True:
    page=input('Please, input number of pages (less than 1280):')
    try:
        page=int(page)
        if  (not 0 <page<= 1280):
            raise Exception
        break
    except Exception:
        print('please, try again')
        
    def number(active=True):
        if active:
            def wrap(page):
                l = []
        for l in range(0,list,1):

            a1 = [a[i] for i in range(page)]
            l.append(a1) 
            a = a[page:] 
        return l
    def wrapper(*args, **kwargs):
                m = [i for i in range(1, page + 1)]
                page(*args, **kwargs)
                return m

@number(active=True)
def number():
    @number(active=False)
    def wrap():
        print(wrap)

#не ставте 0 будь ласка, я дуже не хочу на залікову кр
#я тут намагалась розписати те, що зрозуміла з методички