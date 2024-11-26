import PropTypes from "prop-types";
import { useEffect } from "react";
import { auth, db } from "../../firebase/firebase";
import { getDoc, doc } from "firebase/firestore";

import "./hero.css";

const Hero = ({ userDetails, setUserDetails }) => {
  const fetchUserDetails = async () => {
    auth.onAuthStateChanged(async (user) => {
      // Get the user information
      if (user) {
        const docRef = doc(db, "Users", user.uid);
        const docSnap = await getDoc(docRef);

        if (docSnap.exists()) {
          setUserDetails(docSnap.data());
        } else {
          console.log("No such document!");
        }
      } else {
        console.log("No user signed in!");
        // Redirect to the login page if the user is not logged in
        window.location.replace("/");
      }
    });
  };

  useEffect(() => {
    let ignore = false;

    if (!ignore) {
      fetchUserDetails();
      ignore = true;
    }
  }, []);

  return (
    <>
      {userDetails ? (
        <div>
          <h1>Welcome, {userDetails?.firstName}!</h1>
          <p>Your email: {userDetails?.email}</p>
          <p>Your phone number: {userDetails?.phoneNumber}</p>
          <p>Your address: {userDetails?.address}</p>
          <p>Your birthday: {userDetails?.birthday}</p>
        </div>
      ) : (
        ""
      )}
    </>
  );
};

Hero.propTypes = {
  userDetails: PropTypes.object,
  setUserDetails: PropTypes.func,
};

export default Hero;
