---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

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
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: "Software Engineer"
          company: "Baidu, Inc"
          company_url: "https://home.baidu.com/"
          location: "Beijing, China"
          date_start: "2021-07-07"
          date_end: "2022-06-28"
          # description: """Optimizing the strategies in the crawler system.""" 
        - title: "Research Assistant"
          company: "University of Pittsburgh"
          company_url: "https://www.pitt.edu/"
          location: "Remote"
          date_start: "2020-09-01"
          date_end: "2021-10-01"
          # description: Doing research on quantum circuit simulation using GPUs. Advised by [Prof. Xulong Tang](http://xzt102.github.io/) and [Prof. Jun Yang](https://sites.pitt.edu/~juy9/)
        - title: "Master student"
          company: "Beijing University of Posts and Telecommunications"
          company_url: "https://english.bupt.edu.cn/"
          location: "Beijing, China"
          date_start: "2018-09-01"
          date_end: "2021-06-30"
          # description: Doing research on digital signal processing and machine learning. Advised by [Prof. Zhenming Yu](https://see.bupt.edu.cn/info/1051/1260.htm) and [Prof. Kun Xu](https://www.bupt.edu.cn/info/1075/84950.htm)
          
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
      # Contact (add or remove contact options as necessary)
      email: zyilun8@gmail.com
      # phone: 888 888 88 88
      # appointment_url: 'https://calendly.com'
      # address:
      #   street: 450 Serra Mall
      #   city: Stanford
      #   region: CA
      #   postcode: '94305'
      #   country: United States
      #   country_code: US
      # directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      # office_hours:
      #   - 'Monday 10:00 to 13:00'
      #   - 'Wednesday 09:00 to 10:00'
      # contact_links:
      #   - icon: twitter
      #     icon_pack: fab
      #     name: DM Me
      #     link: 'https://twitter.com/Twitter'
      #   - icon: skype
      #     icon_pack: fab
      #     name: Skype Me
      #     link: 'skype:echo123?call'
      #   - icon: video
      #     icon_pack: fas
      #     name: Zoom Me
      #     link: 'https://zoom.com'
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
      # form:
      #   provider: netlify
      #   formspree:
      #     id:
      #   netlify:
      #     # Enable CAPTCHA challenge to reduce spam?
      #     captcha: false
    design:
      columns: '2'
---
