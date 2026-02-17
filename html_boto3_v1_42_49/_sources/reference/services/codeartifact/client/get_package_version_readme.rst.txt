:doc:`CodeArtifact <../../codeartifact>` / Client / get_package_version_readme

**************************
get_package_version_readme
**************************



.. py:method:: CodeArtifact.Client.get_package_version_readme(**kwargs)

  

  Gets the readme file or descriptive text for a package version.

   

  The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText.

  

  See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/GetPackageVersionReadme>`_  


  **Request Syntax**
  ::

    response = client.get_package_version_readme(
        domain='string',
        domainOwner='string',
        repository='string',
        format='npm'|'pypi'|'maven'|'nuget'|'generic'|'ruby'|'swift'|'cargo',
        namespace='string',
        package='string',
        packageVersion='string'
    )
    
  :type domain: string
  :param domain: **[REQUIRED]** 

    The name of the domain that contains the repository that contains the package version with the requested readme file.

    

  
  :type domainOwner: string
  :param domainOwner: 

    The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

    

  
  :type repository: string
  :param repository: **[REQUIRED]** 

    The repository that contains the package with the requested readme file.

    

  
  :type format: string
  :param format: **[REQUIRED]** 

    A format that specifies the type of the package version with the requested readme file.

    

  
  :type namespace: string
  :param namespace: 

    The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:

     

    .. note::

      

      The namespace is required when requesting the readme from package versions of the following formats:

       

      
      * Maven
       
      * Swift
       
      * generic
      

      

     

    
    * The namespace of a Maven package version is its ``groupId``.
     
    * The namespace of an npm or Swift package version is its ``scope``.
     
    * The namespace of a generic package is its ``namespace``.
     
    * Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
    

    

  
  :type package: string
  :param package: **[REQUIRED]** 

    The name of the package version that contains the requested readme file.

    

  
  :type packageVersion: string
  :param packageVersion: **[REQUIRED]** 

    A string that contains the package version (for example, ``3.5.2``).

    

  
  
  :rtype: dict
  :returns: 
    
    **Response Syntax**

    
    ::

      {
          'format': 'npm'|'pypi'|'maven'|'nuget'|'generic'|'ruby'|'swift'|'cargo',
          'namespace': 'string',
          'package': 'string',
          'version': 'string',
          'versionRevision': 'string',
          'readme': 'string'
      }
      
    **Response Structure**

    

    - *(dict) --* 
      

      - **format** *(string) --* 

        The format of the package with the requested readme file.

        
      

      - **namespace** *(string) --* 

        The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:

         

        
        * The namespace of a Maven package version is its ``groupId``.
         
        * The namespace of an npm or Swift package version is its ``scope``.
         
        * The namespace of a generic package is its ``namespace``.
         
        * Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.
        

        
      

      - **package** *(string) --* 

        The name of the package that contains the returned readme file.

        
      

      - **version** *(string) --* 

        The version of the package with the requested readme file.

        
      

      - **versionRevision** *(string) --* 

        The current revision associated with the package version.

        
      

      - **readme** *(string) --* 

        The text of the returned readme file.

        
  
  **Exceptions**
  
  *   :py:class:`CodeArtifact.Client.exceptions.AccessDeniedException`

  
  *   :py:class:`CodeArtifact.Client.exceptions.InternalServerException`

  
  *   :py:class:`CodeArtifact.Client.exceptions.ResourceNotFoundException`

  
  *   :py:class:`CodeArtifact.Client.exceptions.ThrottlingException`

  
  *   :py:class:`CodeArtifact.Client.exceptions.ValidationException`

  