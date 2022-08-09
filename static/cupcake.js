'use strict';

const BASE_API_URL = "http://localhost:5001/api";

//query API to get cupcakes and add to page

/**
 *get all the cupcakes from the API
 */
async function getCupcakes() {
  const response = await axios.get(`${BASE_API_URL}/cupcakes`);
  return response;
}

/**
 * show all the cupcakes in the HTML
 */
async function showCupcakes() {
  let response = await getCupcakes();
  let cupcakes = response.data.cupcakes;
  for (let i = 0; i < cupcakes.length; i++) {
    $('#cupcakes').append(
      `<li>${cupcakes[i].flavor}
          ${cupcakes[i].rating}
          ${cupcakes[i].size}
          <img class="img-thumbnail" src="${cupcakes[i].image}">

    </li>`);
  }
}
//use jquery to create new image,li...

/**
 * submit new cupcake to the API
 * @returns an object of the cupcake's properties from the response from the post request
 */
async function submitNewCupcake() {
  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();
  let response = await axios.post(`${BASE_API_URL}/cupcakes`,
                      {flavor , size, rating, image})

  return response.data.cupcake
}

/**
 * show the new cupcake on HTML
 */
function appendNewCupcake(cc) {

  $('#cupcakes').append(
    `<li>${cc.flavor}
        ${cc.rating}
        ${cc.size}
        <img class="img-thumbnail" src="${cc.image}">
  </li>`);
}

/**
 * call the submitNewCupcake function to send the data to the API,
 * and display it on HTML
 */
  async function handleSubmit(evt) {
    evt.preventDefault();
    let newCupcake = await submitNewCupcake();
    appendNewCupcake(newCupcake)


  }

/** attach event handler to the form */
$("#add-form").on("submit", handleSubmit)

