var nameList = [
    'Time',
    'Past',
    'Future',
    'Dev',
    'Fly',
    'Flying',
    'Soar',
    'Soaring',
    'Power',
    'Falling',
    'Fall',
    'Jump',
    'Cliff',
    'Mountain',
    'Rend',
    'Red',
    'Blue',
    'Green',
    'Yellow',
    'Gold',
    'Demon',
    'Demonic',
    'Panda',
    'Cat',
    'Kitty',
    'Kitten',
    'Zero',
    'Memory',
    'Trooper',
    'XX',
    'Bandit',
    'Fear',
    'Light',
    'Glow',
    'Tread',
    'Deep',
    'Deeper',
    'Deepest',
    'Mine',
    'Your',
    'Worst',
    'Enemy',
    'Hostile',
    'Force',
    'Video',
    'Game',
    'Donkey',
    'Mule',
    'Colt',
    'Cult',
    'Cultist',
    'Magnum',
    'Gun',
    'Assault',
    'Recon',
    'Trap',
    'Trapper',
];

class Platform{
    constructor(resources){
        this.resources = resources;
        this.floorStatus = floorStatus;
    }
    consume(amount){
        this.resources -= amount;
    }
}

class Floor{
    constructor(lvl,peopleCount){
        this.lvl = lvl;
        this.peopleCount = peopleCount;
    }
    
    procces_platform(platform){
        console.log("korrus", this.lvl)
        this.peopleCount.forEach((person)=>{
            person.makeDecision(platform);
        });
        console.log("resurside jääk", platform.resources);
    }
}

class Person{
    constructor(name, pertcent){
        this.name = name;
        this.pepertcent = pertcent;
    }

    makeDecision(Platform){
        let change = Math.random * 100
        if (change < this.pepertcent && Platform.resources > 0){
            const eatAmount = 10
            platform.consume(eatAmount);
            console.log(this.name,"sõid ", eatAmount ,"toitu");
        }
    }
}

let floors = []
for(let i = 0;i <= 10; i++){
    let person1 = new Person(
        nameList[Math.floor( Math.random() * nameList.length )],
        Math.floor(Math.random() * 100) + 1 +"%"
    );

    let person2 = new Person(
        nameList[Math.floor( Math.random() * nameList.length )],
        Math.floor(Math.random() * 100) + 1 +"%"
    );
    let floor = new Floor(i, [person1, person2])
    floors.push(floor);
}

console.log(floors);

let platform = new Platform(100);

floor.forEach((floor) => {
    floor.procces_platform(platform)
});

