# JSON2NSDictionary
Translate JSON to OC static constant

#### eg:

```json
{
    "people": [
        {
            "firstName": "Brett",
            "lastName": "McLaughlin"
        },
        {
            "firstName": "Jason",
            "lastName": "Hunter"
        }
    ]
}
```

to

```objective-c
@{
	@"people" : @[
		@{
			@"firstName" : @"Brett",
			@"lastName" : @"McLaughlin",
		},
		@{
			@"firstName" : @"Jason",
			@"lastName" : @"Hunter",
		},
	],
	}
```

#### How to use:

```
curl -O https://raw.githubusercontent.com/WarwickZhang/JSON2NSDictionary/master/JSON2NSDictionary.py
python JSON2NSDictionary.py -i <Your JSON File>
```

