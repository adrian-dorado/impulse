import React from 'react';
import Carousel from '../helpers/Carousel';

function MainPage() {
    return (
        <>
            <div style={{}} className="inline-block text-center">
                <h1 className='rounded mt-5 mb-4 py-4 display-5 fw-bold nameText'>Your one stop shop for anything you might need! 💖</h1>
                <hr className='featurette-divider mb-4'></hr>
            </div>
            <div className='pb-5 container'>
                <div className='row'>
                    <div className='col b_cards me-3 shad_bottom p-4 rounded mt-4 heliotrope_gray'>
                        <h1 className='nameText text-left'>Thing of The Month</h1>
                        <hr className="featurette-divider" />
                        <h3 className='siteText text-decoration-underline'>Field Notes Wallet + Notepad and Pen</h3>
                        <p className='nameText'>Over here at Impulse, our memory isn't exactly what you'd call the best
                            but we're sure to never forget a thing with these Field Notes notepads and wallets. <br />
                            We're happy we can provide you with that blissful experience of remembering that
                            fun recipe you thought of, that awkward dad joke, or that brilliant line of code.
                            <br />
                            <br />
                            Memory, but make it aesthetic; only available in this month's "Back-To-Basics" Things Box.
                        </p>
                        <hr className="featurette-divider" />
                        <img className="card b_cards shad_light" width="100%" height="80%" src='field_notes.png' alt='no things :(' aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"></img>
                    </div>
                    <div className='col b_cards ms-3 shad_bottom p-4 rounded mt-4 heliotrope_gray'>
                        <h1 className='nameText text-right'>Style of The Month</h1>
                        <hr className="featurette-divider" />
                        <h3 className='siteText text-decoration-underline'>The Timex California Collection</h3>
                        <p className='nameText'>This watch speaks for itself, but we'll try to say a bit more about it because of how much we love it here.
                            The Timex California collection is full of <i>wonderful</i> colors for anyone who wants
                            to add a pop of color to their life and have a beautiful timepiece anywhere they're going. <br />
                            <br />
                            Timeless style for a modern age; only available in this month's "Pop" Styles box.
                        </p>
                        <hr className="featurette-divider" />
                        <img className="card b_cards shad_light" width="100%" height="80%" src='timex.png' alt='no clothes :(' aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"></img>
                    </div>
                </div>
            </div>
            <Carousel />
        </>
    );
};

export default MainPage;
