# Data models

## Users
| Name | Type | Unique | Optional |
|-|-|-|-|
| first_name | string | no | no |
| last_name | string | no | no |
| username | string | yes | no |
| home_address | string | no | no |
| email_address | string | yes | no |
| password | string | no | no |

The user entity is for customers and potential customers logging in, shopping, and eventually checking out.
___
` `
` `
` `

## Subscription product boxes

| Name | Type | Unique | Optional |
|-|-|-|-|
| username | reference to users | no | no |
| products | reference to products api | no | no |

The subscription product boxes entity refers to the users table for table name, and we'll use an external api to generate products for the monthly product box.
___
`  `
`  `
`  `

## Subscription fashion boxes

| Name | Type | Unique | Optional |
|-|-|-|-|
| username | reference to users | no | no |
| clothing | reference to products api | no | no |
| accessories | reference to products api | no | no |

The subscription fashion boxes entity refers to the users table for table name, and we'll use an external api to generate both clothing and accessories for the monthly product box.


A more detailed version of the data-model can be found here:

![Color-Coded Model Page](wireframes/color_coded_models_guide.png)
