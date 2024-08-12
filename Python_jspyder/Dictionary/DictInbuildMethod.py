
sampleDict={1:"saurabh", 2:"Kumar", 3:"Python", 4: 79, 5: 78.37, 6: "87"};
class DictInbuildMethod:
    def display(self):
        print(sampleDict);


    def dictCopy(self):

        print("\n***** Copy Method ******");
        dCopy=sampleDict.copy();
        print(dCopy);


    def dictItems(self):
        print("\n ***** dictItems");

        ditems=sampleDict.items();
        print(ditems);


    def dectKeys(self):
        print("\n *********** Dict. Keys ****");

        dKeys=sampleDict.keys();
        print(dKeys);


    def dectGet(self):
        print("\n ********** Dict. Get Method ************");

        dget=sampleDict.get(3);
        print(dget);


    def dictFromKey(self):
        print("\n *********** Dict. from Key ***********");

        dfkey=sampleDict.fromkeys("Python");
        print(dfkey);


    def dictValues(self):
        print("\n ************ Dict. Values **************");

        dvalues=sampleDict.values();
        print(dvalues);

    def dictPop(self):
        print("\n ********** Dict. Pop *************");

        dpop=sampleDict.pop(2);
        print(dpop);

    def dpopItem(self):
        print("\n ******** Dict. PopItems *********");

        dpopItem=sampleDict.popitem();
        print(dpopItem);


    def dupdate(self):
        print("\n ************* Dict. Update ************");

        dupdate=sampleDict.update({1:"Prashant"});
        print(dupdate);

    def dclear(self):
        print("\n ************ Dict. Clear ************");

        sampleDict.clear();
        print(sampleDict);



d=DictInbuildMethod();

d.display();

d.dictCopy();
d.display();

d.dictPop()
d.display()


d.dectGet()
d.display()

d.dupdate()
d.display()

d.dectKeys()
d.display()

d.dictFromKey()
d.display()

d.dictValues()
d.display()

d.dictItems()
d.display()

d.dclear()
d.display()



