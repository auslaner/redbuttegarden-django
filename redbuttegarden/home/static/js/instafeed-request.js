const access_token = "EAAHc3xMKegsBAGK7vcWQT6NntJZCmiZAZCZBqUNlN4yomeOhy6sxLu0SRft13fR5Lcps4AeXZCEU2A5YuZCC3tc4BgKbUqkjG0AEfZACpiT9HQjUtyH8ImZBkFO9IgUUjYPaKECkcxOIXNXvBy8xM4bQOAMTv30NGo6JZBK3ERNPtjooat63z2UTJSvmSkRLTihyEYO7Ya3YJvszmkOixX118xubCazKMVDMZD"
const ig_user = "17841401164963561"

fetch(`https://graph.facebook.com/v11.0/${ig_user}/media?access_token=${access_token}`)
    .then(res => res.json())
    .then(json => {
        const ids = []
        for (let obj of json["data"])
            ids.push(obj.id)

        return ids
    })
    .then(ids => {
        for (let id of ids) {
            fetch(`https://graph.facebook.com/v11.0/${id}?fields=media_url, caption, permalink, media_type
                &access_token=${access_token}`)
                .then(res => res.json())
                .then(post => {
                    const media_url = (post.media_type === "IMAGE" ? post.media_url : "")
                    const permalink = (post.media_type === "IMAGE" ? post.permalink : "")
                    const caption = (post.media_type === "IMAGE" ? post.caption : "")

                    let container = document.getElementById("images-container")
                    let mediaParent = document.createElement('div')
                    mediaParent.id = "media-parent"

                    let mediaLink = document.createElement('a')
                    mediaLink.href = permalink
                    mediaLink.id = "media-link"
                    mediaLink.style = "text-decoration: none;"

                    let mediaImg = document.createElement('img')
                    mediaImg.id = "media-img"
                    
                    if (media_url != "") mediaImg.src = media_url 
                    else mediaParent.style = "display: none;"

                    mediaImg.style = (window.matchMedia("(max-width: 420px) and (max-height: 740px)").matches 
                        ? "width: 150px; height: 150px;" 
                        : "width: 350px; height: 350px;")

                    let mediaCaption = document.createElement('p')
                    mediaCaption.innerHTML = caption
                    mediaCaption.style = "color: black;"

                    container.appendChild(mediaParent)
                    mediaParent.appendChild(mediaLink)
                    mediaLink.appendChild(mediaImg)
                    mediaLink.appendChild(mediaCaption)
                })
        }
    })