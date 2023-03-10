import React, { useState, useEffect } from 'react'

export default function Things() {
    const [products, setProducts] = useState([])
    useEffect(() => {
        fetch(`${process.env.REACT_APP_PRODUCTS}/products/`)
            .then(res => res.json())
            .then(res => setProducts(res.products))
    }, [])

    return (
        <>
            <section className='py-5 rounded b_cards text-center my-5  heliotrope_gray container'>
                <div className='row py-lg-5'>
                    <div className='col-md-8 mx-auto'>
                        <h1 className='display-5 nameText'>All of the things</h1>
                        <p className='lead text-muted'>
                            What could you be getting in your box this month?
                            <br />
                            Sometimes it's a one thing, other times it's a different thing.
                            <br />
                            Whatever it is, you're gonna be excited that it showed up.
                            <br />
                            Below are some of the things you could get in your box this month
                            📦
                        </p>
                    </div>
                </div>
            </section>
            <div className='row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3'>
                {products?.map(product => {
                    return (
                        <>
                            <div className='col'>
                                <div className='card shadow-lg b_cards'>
                                    <img
                                        className='card-img-top'
                                        width='100%'
                                        height='100%'
                                        src={product.picture_url}
                                        alt='a product'
                                    ></img>
                                    <div className='card-body nameText text-center heliotrope_gray cards-text-box'>
                                        <h4 className='siteText'>{product.name}</h4>
                                        <hr className='featurette-divider' />
                                        <p className='card-text'>{product.description}</p>
                                    </div>
                                </div>
                            </div>
                        </>
                    )
                })}
            </div>
        </>
    )
}
