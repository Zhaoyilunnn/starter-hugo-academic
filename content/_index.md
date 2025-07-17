---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: experience
    content:
      title: Experience
      # Date format for experience
      date_format: Jan 2006
      items:
        - title: "Software Engineer"
          company: "Baidu, Inc"
          company_url: "https://home.baidu.com/"
          location: "Beijing, China"
          date_start: "2021-07-07"
          date_end: "2022-06-28"
        - title: "Research Assistant. Advisor: [Prof. Xulong Tang](http://xzt102.github.io/) and [Prof. Jun Yang](https://sites.pitt.edu/~juy9/)"
          company: "University of Pittsburgh"
          company_url: "https://www.pitt.edu/"
          location: "Remote"
          date_start: "2020-09-01"
          date_end: "2021-10-01"
        - title: "Master Student. Advisor: [Prof. Zhenming Yu](https://see.bupt.edu.cn/info/1051/1260.htm) and [Prof. Kun Xu](https://www.bupt.edu.cn/info/1075/84950.htm)"
          company: "Beijing University of Posts and Telecommunications"
          company_url: "https://english.bupt.edu.cn/"
          location: "Beijing, China"
          date_start: "2018-09-01"
          date_end: "2021-06-30"
    design:
      columns: '2'
  - block: collection
    id: publication
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        Please feel free to contact me if you are interested in my work. 
      email: zyilun8@gmail.com
      autolink: true
    design:
      columns: '2'
---
