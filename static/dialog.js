
;(function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"))

  
    htmx.on("htmx:afterSwap", (e) => {
      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "dialog") {
        modal.show()
      }
    })
  
    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })
  
    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("dialog").innerHTML = ""
    })
  })()

  
  // The purpose of this function is to have sceond modal only on view mode, it may be redundant but for the moment does the job
  ;(function () {
    const modal = new bootstrap.Modal(document.getElementById("second-modal"))
    
  
    htmx.on("htmx:afterSwap", (e) => {

      // Response targeting #dialog => show the modal
      if (e.detail.target.id == "view-dialog") {
        modal.show()
      }
    })
  
    htmx.on("htmx:beforeSwap", (e) => {
      // Empty response targeting #dialog => hide the modal
      if (e.detail.target.id == "view-dialog" && !e.detail.xhr.response) {
        modal.hide()
        e.detail.shouldSwap = false
      }
    })
  
    // Remove dialog content after hiding
    htmx.on("hidden.bs.modal", () => {
      document.getElementById("view-dialog").innerHTML = ""
    })
  })()


// This condition is not scalable, we need to come with different solution
if(!window.location.href.endsWith("customers/")){
;(function () {
  htmx.on("htmx:afterOnLoad", () => {
    const registration_expiration_date = document.getElementsByClassName("registration_expiration_date")

    registration_expiration_date[0].innerHTML
    for (var i = 0; i < registration_expiration_date.length; i++) {
      expiration_date = new Date(registration_expiration_date[i].innerHTML.replace(/[.,]/g,""))
      const today = new Date();

      if (today > expiration_date){ 
        registration_expiration_date[i].style.background = 'rgba(255,0,0,0.5)';
      }
    }
  })            

})()}