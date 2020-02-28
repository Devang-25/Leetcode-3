```javasc

<!DOCTYPE html>



  


<html class="theme-next mist use-motion" lang="">
<head><meta name="generator" content="Hexo 3.8.0">
  <!-- hexo-inject:begin --><!-- hexo-inject:end --><meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta name="theme-color" content="#222">









<meta http-equiv="Cache-Control" content="no-transform">
<meta http-equiv="Cache-Control" content="no-siteapp">
















  
  
  <link href="/lib/fancybox/source/jquery.fancybox.css?v=2.1.5" rel="stylesheet" type="text/css">







<link href="/lib/font-awesome/css/font-awesome.min.css?v=4.6.2" rel="stylesheet" type="text/css">

<link href="/css/main.css?v=5.1.4" rel="stylesheet" type="text/css">


  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon-next.png?v=5.1.4">


  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32-next.png?v=5.1.4">


  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16-next.png?v=5.1.4">


  <link rel="mask-icon" href="/images/logo.svg?v=5.1.4" color="#222">





  <meta name="keywords" content="Hexo, NexT">










<meta name="description" content="http://www.1point3acres.com/bbs/thread-210460-1-1.htmlhttp://wdxtub.com/interview/14520850399861.html 成功不可复制，但是失败总是一样的：http://www.1point3acres.com/bbs/thread-203776-1-1.htmlhttp://www.1point3acres.com">
<meta property="og:type" content="article">
<meta property="og:title" content="Interview-Amazon-OA1-Logic">
<meta property="og:url" content="http://yoursite.com/2017/09/03/Interview/Interview-Amazon-OA1-Logic/index.html">
<meta property="og:site_name" content="Beyond">
<meta property="og:description" content="http://www.1point3acres.com/bbs/thread-210460-1-1.htmlhttp://wdxtub.com/interview/14520850399861.html 成功不可复制，但是失败总是一样的：http://www.1point3acres.com/bbs/thread-203776-1-1.htmlhttp://www.1point3acres.com">
<meta property="og:locale" content="default">
<meta property="og:updated_time" content="2018-07-15T03:58:39.464Z">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Interview-Amazon-OA1-Logic">
<meta name="twitter:description" content="http://www.1point3acres.com/bbs/thread-210460-1-1.htmlhttp://wdxtub.com/interview/14520850399861.html 成功不可复制，但是失败总是一样的：http://www.1point3acres.com/bbs/thread-203776-1-1.htmlhttp://www.1point3acres.com">



<script type="text/javascript" id="hexo.configurations">
  var NexT = window.NexT || {};
  var CONFIG = {
    root: '/',
    scheme: 'Mist',
    version: '5.1.4',
    sidebar: {"position":"left","display":"post","offset":12,"b2t":false,"scrollpercent":false,"onmobile":false},
    fancybox: true,
    tabs: true,
    motion: {"enable":true,"async":false,"transition":{"post_block":"fadeIn","post_header":"slideDownIn","post_body":"slideDownIn","coll_header":"slideLeftIn","sidebar":"slideUpIn"}},
    duoshuo: {
      userId: '0',
      author: 'Author'
    },
    algolia: {
      applicationID: '',
      apiKey: '',
      indexName: '',
      hits: {"per_page":10},
      labels: {"input_placeholder":"Search for Posts","hits_empty":"We didn't find any results for the search: ${query}","hits_stats":"${hits} results found in ${time} ms"}
    }
  };
</script>



  <link rel="canonical" href="http://yoursite.com/2017/09/03/Interview/Interview-Amazon-OA1-Logic/">





  <title>Interview-Amazon-OA1-Logic | Beyond</title><!-- hexo-inject:begin --><!-- hexo-inject:end -->
  








</head>

<body itemscope="" itemtype="http://schema.org/WebPage" lang="default">

  
  
    
  

  <!-- hexo-inject:begin --><!-- hexo-inject:end --><div class="container sidebar-position-left page-post-detail">
    <div class="headband"></div>

    <header id="header" class="header" itemscope="" itemtype="http://schema.org/WPHeader">
      <div class="header-inner"><div class="site-brand-wrapper">
  <div class="site-meta ">
    

    <div class="custom-logo-site-title">
      <a href="/" class="brand" rel="start">
        <span class="logo-line-before"><i></i></span>
        <span class="site-title">Beyond</span>
        <span class="logo-line-after"><i></i></span>
      </a>
    </div>
      
        <p class="site-subtitle"></p>
      
  </div>

  <div class="site-nav-toggle">
    <button>
      <span class="btn-bar"></span>
      <span class="btn-bar"></span>
      <span class="btn-bar"></span>
    </button>
  </div>
</div>

<nav class="site-nav">
  

  
    <ul id="menu" class="menu">
      
        
        <li class="menu-item menu-item-home">
          <a href="/" rel="section">
            
              <i class="menu-item-icon fa fa-fw fa-home"></i> <br>
            
            Home
          </a>
        </li>
      
        
        <li class="menu-item menu-item-about">
          <a href="/about/" rel="section">
            
              <i class="menu-item-icon fa fa-fw fa-user"></i> <br>
            
            About
          </a>
        </li>
      
        
        <li class="menu-item menu-item-categories">
          <a href="/categories/" rel="section">
            
              <i class="menu-item-icon fa fa-fw fa-th"></i> <br>
            
            Categories
          </a>
        </li>
      
        
        <li class="menu-item menu-item-archives">
          <a href="/archives/" rel="section">
            
              <i class="menu-item-icon fa fa-fw fa-archive"></i> <br>
            
            Archives
          </a>
        </li>
      

      
        <li class="menu-item menu-item-search">
          
            <a href="javascript:;" class="popup-trigger">
          
            
              <i class="menu-item-icon fa fa-search fa-fw"></i> <br>
            
            Search
          </a>
        </li>
      
    </ul>
  

  
    <div class="site-search">
      
  <div class="popup search-popup local-search-popup">
  <div class="local-search-header clearfix">
    <span class="search-icon">
      <i class="fa fa-search"></i>
    </span>
    <span class="popup-btn-close">
      <i class="fa fa-times-circle"></i>
    </span>
    <div class="local-search-input-wrapper">
      <input autocomplete="off" placeholder="Searching..." spellcheck="false" type="text" id="local-search-input">
    </div>
  </div>
  <div id="local-search-result"></div>
</div>



    </div>
  
</nav>



 </div>
    </header>

    <main id="main" class="main">
      <div class="main-inner">
        <div class="content-wrap">
          <div id="content" class="content">
            

  <div id="posts" class="posts-expand">
    

  

  
  
  

  <article class="post post-type-normal" itemscope="" itemtype="http://schema.org/Article">
  
  
  
  <div class="post-block">
    <link itemprop="mainEntityOfPage" href="http://yoursite.com/2017/09/03/Interview/Interview-Amazon-OA1-Logic/">

    <span hidden itemprop="author" itemscope="" itemtype="http://schema.org/Person">
      <meta itemprop="name" content="Wayne">
      <meta itemprop="description" content="">
      <meta itemprop="image" content="/images/avatar.gif">
    </span>

    <span hidden itemprop="publisher" itemscope="" itemtype="http://schema.org/Organization">
      <meta itemprop="name" content="Beyond">
    </span>

    
      <header class="post-header">

        
        
          <h1 class="post-title" itemprop="name headline">Interview-Amazon-OA1-Logic</h1>
        

        <div class="post-meta">
          <span class="post-time">
            
              <span class="post-meta-item-icon">
                <i class="fa fa-calendar-o"></i>
              </span>
              
                <span class="post-meta-item-text">Posted on</span>
              
              <time title="Post created" itemprop="dateCreated datePublished" datetime="2017-09-03T22:32:57+00:00">
                2017-09-03
              </time>
            

            

            
          </span>

          
            <span class="post-category">
            
              <span class="post-meta-divider">|</span>
            
              <span class="post-meta-item-icon">
                <i class="fa fa-folder-o"></i>
              </span>
              
                <span class="post-meta-item-text">In</span>
              
              
                <span itemprop="about" itemscope="" itemtype="http://schema.org/Thing">
                  <a href="/categories/Interview/" itemprop="url" rel="index">
                    <span itemprop="name">Interview</span>
                  </a>
                </span>

                
                
              
            </span>
          

          
            
              <span class="post-comments-count">
                <span class="post-meta-divider">|</span>
                <span class="post-meta-item-icon">
                  <i class="fa fa-comment-o"></i>
                </span>
                <a href="/2017/09/03/Interview/Interview-Amazon-OA1-Logic/#comments" itemprop="discussionUrl">
                  <span class="post-comments-count disqus-comment-count" data-disqus-identifier="2017/09/03/Interview/Interview-Amazon-OA1-Logic/" itemprop="commentCount"></span>
                </a>
              </span>
            
          

          
          

          

          

          

        </div>
      </header>
    

    
    
    
    <div class="post-body" itemprop="articleBody">

      
      

      
        <p><a href="http://www.1point3acres.com/bbs/thread-210460-1-1.html" target="_blank" rel="noopener">http://www.1point3acres.com/bbs/thread-210460-1-1.html</a><br><a href="http://wdxtub.com/interview/14520850399861.html" target="_blank" rel="noopener">http://wdxtub.com/interview/14520850399861.html</a></p>
<p>成功不可复制，但是失败总是一样的：<br><a href="http://www.1point3acres.com/bbs/thread-203776-1-1.html" target="_blank" rel="noopener">http://www.1point3acres.com/bbs/thread-203776-1-1.html</a><br><a href="http://www.1point3acres.com/bbs/thread-224773-1-1.html" target="_blank" rel="noopener">http://www.1point3acres.com/bbs/thread-224773-1-1.html</a><br><a href="http://www.1point3acres.com/bbs/thread-203921-1-1.html" target="_blank" rel="noopener">http://www.1point3acres.com/bbs/thread-203921-1-1.html</a></p>
<!--想不到时隔半年多，又开始面亚麻了。
http://www.1point3acres.com/bbs/thread-210460-1-1.html
之前OA1挂掉的惨痛经历历历在目。

之前的失败主要有
1. 自以为是，以为别人进亚麻很简单，自己也定然万无一失。 没有足够重视。

2. 轻敌冒进，在OA1还没有完全掌握的情况下，就开始复习OA2了。用兵之道，在于步步为营，稳扎稳打。专注眼前。

3. 只看到别人成功案例，而忽视了失败的情况，幸存者误差。 在查面经的同时，也要查跪经。

4. 失败之后。哀伤感叹，浪费了很多精力与时间。

5. 看似简单的题，限时的面试，考试环境中,往往就很容易做不出来，这种情况就是要求极高的心里素质，和冷静思考的能力。

这让我想到当年明月在明朝那些事里写的名将是怎样练成的，带领几十万人，一个细小的决定可能决定里几十万人的生死，在任何情况下都要保持冷静。
作出正确判断。自己当个班长都当不好，面个试还紧张的要死。真是觉得做英雄的真是非常人，行非常事。
-->
<p>这篇博客来主要目的是搜集尽可能全的亚马逊OA1题目，同学们有啥新题补充，或者发现有误，请email: beyondfengwei@gmail.com<br>所有内容来自互联网网。 侵权则删。</p>
<p>做OA前认真复习，做的时候忘记原题。前面小题抓紧时间。后面大题仔细推敲.<br><a id="more"></a></p>
<h3 id="推理"><a href="#推理" class="headerlink" title="推理"></a>推理</h3><p>虽然大多数的推理题，都是转化为数字，但是字母题侧重于位置，间隔，奇偶，映射。<br>而数字题侧重于数学推导，求和，平方，斐波拉契额数列，按位与，n^2,n^3, n^3 - n, n^n, 2^n,倍数</p>
<h5 id="字母推理"><a href="#字母推理" class="headerlink" title="字母推理"></a>字母推理</h5><p>• D, H, L, (p) (P，等间距)</p>
<p>• QPS : TSV -&gt; IHK : (LKN) 都是+3</p>
<p>• EAGLE : FZHKF -&gt; THANKS : (UGBMLR) +1, -1 找规律的(<strong>奇数+1偶数- 1</strong>)</p>
<p>• FASTER : HCUVGT -&gt; SLOWER —&gt; (UNQYGT) (+2)</p>
<p>• ADBC : EHFG -&gt; ILJK : (MPNO)(4个字母一组,ABCD,再将最后一个D放到第二个位置)</p>
<p>• JOHN : LSNV -&gt; MARK : (OEXS)(+2 +4 +6 +8)</p>
<p>• COMPUTER : PMOCRETU -&gt; TELEVISION : (VELETNOISI)(<strong>先均分成两半，对每一半的字母顺序进行颠倒</strong>)</p>
<p>• A17R : D12P -&gt; G7N : (J7Q) (R=A+17, J=G+3)<br>A17R: D12P - &gt; G7N: J2L （R=A+17, 17 – 12 = 5）</p>
<p>• COMPUTER : GKQLYPIN -&gt; SENATE : WARWXA(奇数+4偶数-4)</p>
<p>• KPQR : LRTV -&gt; DGHY : (EIKC) (前后相减每一位的增加分别为1,2,3,4)</p>
<p>• ACFJ : CEHL -&gt; PRUY : (RTWA) (前后相减每一位的增加分别为1,2,3,4)</p>
<p>• VAILANT : UBKJZOS -&gt; TRANSCEND : SSCLRDGLC (面经有误，奇数对:奇数-1，偶数+1，偶数对:奇数-2，偶数+2)</p>
<p>• VALIANT : UBKJZOS :: TRANSCEND -&gt; SSZORDDOC  (奇数-1,偶数 +1)</p>
<p>• MQD : KRK -&gt; SWM : ( QXT) (13, 17, 4, 11, 18, 11 =&gt; 13 - 18 = -5, 17 - 11 = 6, 4 - 11 = -7；5,6,7连续,正负号交替；另一个answer是NCF) 注意最后的位置</p>
<p>MQD:KRK   SWM: TXQ（13, 17,  4；11, 18, 11交叉（13-18）（17-11） （4-11））<br>• AD5 : ED9 求和</p>
<p>• ASSERTIVENESS-&gt; SENSSAEVISTRE : MULTINATIONAL -&gt; ?<br>(记录ASSERTIVENESS每个字母的位置，再记录下SENSSAEVISTRE每个字 母的位置，找出mapping关系(比如A在ASSERTIVENESS中第一个位 置，在SENSSAEVISTRE第六个位置，那么1-&gt;6)。最后记录 MULTINATIONAL每个字母的顺序，按照之前找出的mapping对找出来 (如M肯定会在所求字符串的第六个位置)。这种题字符串的长度和所 包含的字母个数肯定是一样的。)<br>重复字母的情况是有一定规律的:ASSERTIVENESS-&gt; SENSSAEVISTRE , 123456789,10,11,12,13 -&gt; 12,11,10,3,2,1,9,8,7,13,6,5,4 (用重复的字母把字符串隔开，就能看到排 列顺序了)【2】ass 【5】ert 【3】ive 【1】nes 【4】s</p>
<p>ASS ERT IVE NES S<br>SEN SSA EVI S TRE </p>
<p>MUL TIN ATI ONA L<br>ANO LUM ITA L NIT</p>
<p>• 原题字母，这里直接用数字表示:4，5，12，8，9 =&gt; 3，4，1，7，8问 13, 21, 13, 2, 1, 9 =&gt; ?<br>(网上解法有:<br>4, 5, 12, 8, 9 =&gt; (4 - 1), (5 - 1), (1 - 0)(2 - 1), (8 - 1), (9 - 1)，so13, 21, 13, 2, 1, 9 =&gt; 02, 10, 02, 1, 0,8<br>或者<br>4 5 12 8 9 -&gt; 3 4 1 7 8 (每位都-1) 13 21 13 2 1 9 -&gt; 02 10 02 1 26 8 就是2 10 2 1 26 8 (B J B A Z H)</p>
<p>ACG-&gt;HJN DGM-&gt; KNT （a1’ – a1 = 7, a2’ – a2 = 7, a3’ – a3 = 7）<br>ADGJM: PSXRV(FINRV) : KNQTW : PSVYB 其他都是差2，选第二个<br>AFK : TWB : PUZ : DIN (间隔4)<br>AZP: ZAR :: TXK: SYM (-1, +1, +2)<br>bb c MN : dd e OP : gg f QP : mm n WX (第二个字母是第一出现字母的后一个)<br>BAD: FEH, POS, TSV (-1, +3)<br>BCEH : PQSV : CDGK : STVY (第二三位间隔2)<br>BECD: FTGH :: JMKL : NQOP 同上，+4<br>BHE : FLI =&gt; JPM :(NTQ) (每位+4)<br>CEH : PRV: TVY: MOR (间隔：+2, +3)<br>DEB: FGD: PQN: TUR  (第二位第三位差3)<br>DELHI : CDAGH =&gt;MUMBAI : BJBAZH<br>DICE : 3824 =&gt;EDGE : 4364 (每位减1)<br>DJ:  WQ =&gt;  FK : UP (DJ +6, WQ -6; FK + 5, UP -5)<br>EXAM: FYBN :: TEST :  UFTU (+1)<br>FHKO,CEHL, ZBEJ, XZCG 数字+2 +3 +4.<br>KML : PRQ: NPQ : TVU (第三位是第一和第二位间隔的字母)<br>LOMN : HJIK: QTRS : UXVW (第一位和第二位差3)<br>MARKET-&gt;12-26-17-10-4-19. PRODUCT: 15,17,14,3,20,2,19(-1)<br>NORMAL : LAMRON =&gt;SYSTEM : (METSYS)就是把字母顺序倒过来<br>POM,KJH, TSQ, VUS 数字-1-2<br>QDXM : SFYN :: UIOZ :WKPA (a1’ = a1+2, a2’ = a2+2, a3’=a3+1, a4’ = a4+1)<br>QSV :CFK : PSX : RUZ<br>SOUP: RPTQ =&gt; TOUR: SPTS (-1, +1, -1, +1)<br>STUMP : PQRJM =&gt; PITCH: MFQZE (每位减3)<br>TENNIS : UDOMJR =&gt;CRICKET : DQJBLDU (+1, -1)</p>
<h5 id="数字推理"><a href="#数字推理" class="headerlink" title="数字推理"></a>数字推理</h5><h5 id="间隔"><a href="#间隔" class="headerlink" title="间隔"></a>间隔</h5><h6 id="简单间隔"><a href="#简单间隔" class="headerlink" title="简单间隔"></a>简单间隔</h6><p>• 46 : 64 -&gt; 82 : (100) (差为18)</p>
<p>• 3,6,18,108,(1944) (18 * 6 = 108，所以应该是18 * 108)</p>
<h6 id="按位间隔"><a href="#按位间隔" class="headerlink" title="按位间隔"></a>按位间隔</h6><p>• 985 : 874 -&gt; 763 : (652) (每一位减一即可)</p>
<p>• 865 : 532 -&gt; 976 : (643) (右边是左边每一位减三)</p>
<h6 id="奇偶间隔"><a href="#奇偶间隔" class="headerlink" title="奇偶间隔"></a>奇偶间隔</h6><p>• 2,3,7,8,13,14,(20) (相差1,4,1,5,1,6)</p>
<p>• 2 8 5 6 8 (4) 11 (分奇偶, 2、5、8、11， 加3得来的。另外一组应该是减2，也就是8、6、4)</p>
<p>• 0 2 3 5 8 10 15 17 24 26 -&gt; 35  (+2,+1,+2,+3,+2,+5,+2,+7,+2,+9)</p>
<h6 id="递增间隔"><a href="#递增间隔" class="headerlink" title="递增间隔"></a>递增间隔</h6><p>• 3 7 13 21 (31) (间隔4,6,8,10)</p>
<p>• 5 11 19 29 (41) (间隔6,8,10,12)</p>
<p>• 0, 2, 6, 12, 20, (30)（间隔2，4，6，8）</p>
<p>• 0, 3, 8,15 -&gt; 24 (间隔3,5,7,9)</p>
<p>• 82, 97, 114, 133, (154) (间隔15, 17, 19, 21)</p>
<p>• 10 74 202 394 650 (间距递增64，64，128，192，256)</p>
<p>• 3, 11, 25, 45, —&gt; 71 (间隔8 ,14,20,26)</p>
<h5 id="平方-指数-反正就是2-n-3-n-4-n-n-2-n-3-n-4"><a href="#平方-指数-反正就是2-n-3-n-4-n-n-2-n-3-n-4" class="headerlink" title="平方 指数 反正就是2^n, 3^n, 4^n ,n^2, n^3,n^4"></a>平方 指数 反正就是2^n, 3^n, 4^n ,n^2, n^3,n^4</h5><p>• 10 14 23 39 64 (100) (间距为完全平方数)</p>
<p>• 1,1,4,2,13,3,40,4,(121) ( 1+3 ^ 1 = 4，4+3 ^ 2 = 13，13 + 3 ^ 3 = 40，40 + 3 ^ 4 = 121)</p>
<p>• 1 5 7 (8) (1 + 2^2 = 5， 5 + 2^1 = 7 ，7 + 2^0 = 8)</p>
<p>• 3 6 15 42 123 (3 + 3^1 = 6, 6 + 3^2 = 15, 15 + 3^3 = 42, 42+ 3^4 = 123)</p>
<p>• 1:4:27:256:3125 (n^n)</p>
<p>• 2, 5, 26，(677) (规律是当前数字是前一个数字平方加1)</p>
<h5 id="求和，斐波拉契数列"><a href="#求和，斐波拉契数列" class="headerlink" title="求和，斐波拉契数列"></a>求和，斐波拉契数列</h5><p>• 27 : 24 -&gt; 64 : (60)(27=3^3,3^3-3=24,64=4^3,4^3-4=60)</p>
<p>• 0 1 1 2 4 8 (16)(16前面的所有数加起来)</p>
<p>• 8, 8, 15, 23, 38, (61)</p>
<p>• 0 1 1 2 3 7 22 (0 * 1 + 1 = 1, 1 * 1 + 1 = 2, 1 * 2+ 1 =3, 2 * 3+1 = 7, 3 * 7 + 1 = 22)</p>
<h4 id="递推表达式"><a href="#递推表达式" class="headerlink" title="递推表达式"></a>递推表达式</h4><p>• 24 : 50 =&gt; 102 : 206 ( x * 2 + 2)</p>
<p>• 5, 9, 16, 29, (54)（9 = 5*2 – 1, 16 = 9 * 2 – 2, 29 = 16*2 – 3,）</p>
<p>• 4,12,6,18,12,36,30, 90（4 * 3 = 12,12 - 6 = 6,6 * 3= 18,18 - 6= 12,12 * 3= 36,36 - 6=30）</p>
<p>• 0.28 0.56 1.68 (6.72) (0.56 = 0.28 * 2, 1.68 = 0.56 * 3, 6.72 = 1.68 * 4)</p>
<p>• 3, 15, 35, 63, (99) (3 = 1 * 3, 15 = 3 * 5, 35 = 5 * 7, 63 = 7 * 9, 99 = 9 * 11)</p>
<h5 id="居然还有质数"><a href="#居然还有质数" class="headerlink" title="居然还有质数"></a>居然还有质数</h5><p>• 16 30 46 62 82（13+3， 29+1， 43+3， 61+1 然后前面的都是质数，每个质数之间隔了三个质数， 61之后第四个质数是79， 79+3=82，或者16加上后面的数为第二个的结果）</p>
<h3 id="排异题"><a href="#排异题" class="headerlink" title="排异题"></a>排异题</h3><p>间距，奇偶，交叉<br>• BGL DIN MRW (HLR) (差5差6, 选HLR)</p>
<p>• PRS TVX FIK (LME) (前三项为递增)</p>
<p>• JLP (LNT) TVZ DFJ (10,12,16; 12,14,20; 20,22,26; 4,6,10; 差2差4递增，面经还有一种解法是首字母是不是4的倍数，我觉的不对，如果只考虑首字母，没必要给出三个字母，这种推理题一般不会给出无用条件)<br>JLP LNT TVZ DFJ（a1+2 = a2, a2+4 = a3, 故选2）</p>
<p>• (ABIJ) DEHI MNQR STWX (ABIJ前后一对间距不同) (1,2,9,10; 4,5,8,9; 13,14,17,18; 19,20,23,24)</p>
<p>• ADP QTS HKR STE (选1?都是完全平方数?，或者QTS，位与的结果不是 0?, 这题个人更偏向于国外网站选的是STE, 顺序加起来不为奇数，像这种题，偏向于 三个 是什么， 另一个不是)</p>
<p>• RHCAI OEST HNDA ADEH(RHCAI?只有这个不是身体部位?)</p>
<p>• ADF MPR ILN EHJ(2?只有它不是以元音开头?)<br>ADF MPR ILN EHJ（元音开头，位与操作，ILN不是0）</p>
<p>• STV XY A KKT BDE(其他都是两偶一奇，只有KKT是两奇一偶)</p>
<p>• AE5 DF6 HN14 KP2(选KP2，因为P!=2)</p>
<p>• HIK DGJ LPT SUW (1，因为不是等间距)</p>
<p>• LKJI (XYWV) WVUT KJIH(其他三个是相邻倒序)</p>
<p>• 956 794 884 678(678，前几组加起来和都是20)</p>
<p>• (1,4,16)  (17,20,24)   (8,11,18)  (19,20,5) (最后一个，间距不是3的倍数)</p>
<h3 id="逻辑推理小题"><a href="#逻辑推理小题" class="headerlink" title="逻辑推理小题"></a>逻辑推理小题</h3><h4 id="自定义表达式。-这题一定要审题清楚，不能想当然。"><a href="#自定义表达式。-这题一定要审题清楚，不能想当然。" class="headerlink" title="自定义表达式。 这题一定要审题清楚，不能想当然。"></a>自定义表达式。 这题一定要审题清楚，不能想当然。</h4><p>例题1.<br>The given signs denote the following operations / relationships</p>
<p>A - B means A plus B<br>A # B means A multipled with B<br>A / B means A is greater than or equal to B<br>A ? B means A is less than B<br>On the basis of this information, and assuming that the given statements are true, find out which of the two conclusions(I and II) is / are definitely true.</p>
<p>Statements<br>(V # X) / (V -X), X ? Y and Z / Y<br>Conclusion:<br>I. X ? Y<br>II. (V - X) ? (V # X)  </p>
<p>• Only conclusion I is true<br>• Only conclusion II is true<br>• Both the conclusion are true<br>• Neither conclusion I nor II is true</p>
<p>注意 - 是 plus, ／ 是 大于等于, ? 是 小于。</p>
<p>例题2.<br>“％” “means greater than;”<br>“&gt;”  “means equal;”<br>“=”  “means is not less than;”<br>“@”  “means not equal;”<br>“#”  “means less than;”<br>“星号”  “means no greater than.”<br>然后给了三个条件：<br>A%B (A &gt; B),  C=E (C &gt;= E), D<em>B (D&lt;=B)，<br>问:<br>1）A#D (根据条件可推出 A &gt;= D, A#D = A &lt; D, 不对)<br>2）C</em>E 里面哪个是成立的（C*E=C &lt; E, 根据条件不对），所以两个都不成立</p>
<p>例题3.<br>The given signs denote the following operations/relationships:<br>“%” denotes “greater than”<br>“&gt;” denotes “equal to”<br>“=” denotes “not less than”<br>“@” denotes “not equal to”<br>“#” denotes “less than”.<br>“*” denotes “not greater than”<br>on the basis of this information and assuming that the given statements are true, find out which of the two conclusions (I and II) is/are definitely true.<br>Statements: P &gt; S, S@T, P#R Conclusion: I. S%R II. P@T<br>A Only conclusion I is true<br>B Only conclusion II is true.<br>C Neither conclusion I nor II is true<br>D Both conclusion I and II are true</p>
<h4 id="走路问题"><a href="#走路问题" class="headerlink" title="走路问题"></a>走路问题</h4><p>这里的take an about-turn, turn around, 都是reverse turn. 向后转的意思。</p>
<ol>
<li><p>If northwest becomes east, northeast becomes south, and so on, what does southeast become? (west)</p>
</li>
<li><p>Lily can’t find her home, she is 25 yards southwest of her home, then she walked 20 yards toward north, where is her home from her now? (15 yards, east)</p>
</li>
<li><p>还有一个面朝北的朋友，先左走15m，然后一个about-turn走了30，这货在哪（about turn指的是向后转。先向西走15m，然后向东走30m，应该在东15m）</p>
</li>
<li><p>小明往东南走4 miles，往西走8 miles， 再往西北走4 miles。现在小明离出发 点是什么方位?(正西8 miles, 平行四边形)</p>
</li>
<li><p><strong>这题是易错题，用笔模拟小明，仔细走一遍<br>小明面朝南，往左走20miles， 再往右走 10miles， 再往左走30miles。 现在 小明离出发点是什么方位?(大致东南方向?)<br>这题居然错了.</strong></p>
</li>
<li><p>小明从原点出发往北走了一段距离，左转走了10再左转走了20，发现自己在出发点西侧10，问一开始往北走了多少？(20) </p>
</li>
<li><p>南5西4南7东4北5，问方向、离原点距离(在原点正南7处)<br>一个人从point 1向south走了20miles，然后turn right， 有向前走了30miles，然后第二次turn right,再向前走了20miles。问第二次turn right后朝什么方向前进。(N)</p>
</li>
<li><p>Consider the direction codes given below:<br>“&gt;” means ‘moves 3 yards to the north’<br>“&lt;” means ‘moves 10 yards to the east’<br>“+” means ‘moves 7 yards to the west’.<br>“-“ means ‘moves 15 yards to the south’<br>What is the new position of ‘Z’ with respect to its initial position if its movement is (Z+Z &gt; Z &lt; Z-)?<br>A 3 yards east and 12 yards north<br>B 3 yards east and 12 yards south<br>C 3 yards west and 12 yards south<br>D 3 yards west and 12 yards north</p>
</li>
<li><p>向东4 miles，向北8miles， 向西2miles， 求最后方位 northeast</p>
</li>
<li><p>A man jogs 4 miles towards east, then 8 miles towards north and from there he goes 2 miles towards west. In which direction is he, from his starting point.<br>A East<br>B North-east<br>C North-west.<br>D  West</p>
</li>
<li><p>Jenny has lost her way home. She was standing 25 yards away from house in the SW direction. Walk 20 yards north and reaches point ‘A’. how far and in which direction would she have to walk to reach her house.. 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴<br>A 20 yards, east<br>B 15 yards, east<br>C 15 yards, west<br>D 20 yards, west</p>
</li>
<li><p>Elijah travelled a distance of 80 miles towards north. Then he turned right and travelled 65 miles. He turned northwards and travelled 45 miles. He travelled further, by turning 45 clockwise. Towards which direction is he driving now?<br>A North<br>B West<br>C South west<br>D North east</p>
</li>
</ol>
<h4 id="楼层坐人问题"><a href="#楼层坐人问题" class="headerlink" title="楼层坐人问题"></a>楼层坐人问题</h4><p>一个楼有3层，每个level 坐一些人，第二层能坐最多，一共坐66个人。给了两个条件求第二层坐了多少人。<br>1，其中有一层坐了21 人。<br>2，第二层比其中一层多座了2人 我选的可以求出第二层多少人， 21，22， 23. 第二层23人。</p>
<p>这题有点小trick, 运用反正法，<br>假如第二层是21人，其中必有一层是19人，剩下一层是26人。 这样第二层至少26个作为，坐19人的那层最多14个座位，坐不下19人。<br>所以只能第二层是23人，其他两层有一个是21,另一个是22，但具体不确定。</p>
<h4 id="年龄问题"><a href="#年龄问题" class="headerlink" title="年龄问题"></a>年龄问题</h4><p>推断一个人的年龄 (1)知道所有人的平均年龄 (2)所有人年龄都一样， 问(1)和(2)怎么来推断这个人的年龄<br>有点奇怪，所有人年龄一样，那不就是平均年龄？</p>
<p>妹妹比哥哥小5岁(或其他数字) ， 哥哥1988年，判断能计算什么(妹妹的年龄，妹妹的出生年)</p>
<h1 id="求日期"><a href="#求日期" class="headerlink" title="求日期"></a>求日期</h1><p>关于亚麻生日问题的原题，有同学知道请发邮件到beyondfengwei@gmail.com<br>生日在9月19~25， leap year，判断能否能计算出生日 ????? (29, common year 28)<br>完全不懂这题在说啥。。<br>说我生日在二月和十月之间，在四月和八月之间，（都是non-inclusive)，你猜猜我生日到底几月啊。（这什么意思。。谁遇到过可以给我解释一下不）</p>
<p>On what date was the car purchased by Lily?<br>Statement:<br>I) certainly before 19 October, 2009 but definitely not before 16 October, 2009<br>II) certainly after 17 October, 2009 but not later than 20 October, 2009. Waral<br>A)I alone is sufficient for answering the question. From 1point 3acres bbs<br>B)II alone is sufficient for answering the question<br>C)Both together are sufficient for answering the question (18th, Oct)<br>D)Both together are not sufficient for answering the question<br>E)Either is sufficient for answering the question</p>
<h4 id="排名问题"><a href="#排名问题" class="headerlink" title="排名问题"></a>排名问题</h4><p>给两个条件： I. 班级总人数38， II 比小王分数低的有19人选 (结合I,II两个条件可以决定小王在班级的排名) </p>
<h4 id="买车问题"><a href="#买车问题" class="headerlink" title="买车问题"></a>买车问题</h4><p>给两个条件: I. 小王买车时间 <10 19="" 且="">=10/16<br>II.小王买车时间 &gt;10/17 且 &lt;=10/20<br>选 (结合I,II 两个条件可以确定小王具体买车时间.) </10></p>
<h4 id="球堆问题"><a href="#球堆问题" class="headerlink" title="球堆问题"></a>球堆问题</h4><p>是桌上一堆球，取掉7个不少于23个， 加上6个不多于20个，问能否推断桌上几个球 (不能，不成立)</p>
<h4 id="电离能"><a href="#电离能" class="headerlink" title="电离能"></a>电离能</h4><p>Problem Question: Ionization energy decreases with the increasing size of metal atoms. Out of cesium, lithium, postassium and sodium, which will have the lowest ionization energy?<br>Statements:<br>I) Lithium has the smallest size<br>II) The size of postassium and cesium is greater than that of lithium.</p>
<p>• Statement I alone is sufficient for answering the problem question<br>• Statement II alone is sufficient for answering the problem question<br>• Both statements put together are sufficient for answering the problem question<br>• Both statements even put together are not sufficient for answering the problem question<br>• Either of the statements is sufficient for answering the problem question</p>
<p>together are not sufficient </p>
<h4 id="买卖冰箱"><a href="#买卖冰箱" class="headerlink" title="买卖冰箱"></a>买卖冰箱</h4><p>问想要求今年有多少个冰箱sold了，需要下述哪几个条件</p>
<ol>
<li>今年售出的冰箱是去年的3倍</li>
<li>去年sold了40个冰箱<br>我的答案是两个条件都需要</li>
</ol>
<h4 id="兴趣小组"><a href="#兴趣小组" class="headerlink" title="兴趣小组"></a>兴趣小组</h4><p>假设人们可以有3种兴趣，且每人至少有一个<br>I. 135个人中，只有5个人有3种兴趣，有100个人有1种兴趣.<br>II. 400个人中，有35个人至少有2种兴趣<br>问，是否能得出exactly 2个兴趣的人数</p>
<p>只有I能得出</p>
<h4 id="哪天买车"><a href="#哪天买车" class="headerlink" title="哪天买车"></a>哪天买车</h4><p>conditions:<br>I. Before 10/19/2009, not before 10/16/2009<br>II. after 10/17/2009, not later than 10/20/2009<br>问LILY哪天买的车？<br>选的I, II两个条件加一起可以得出</p>
<h4 id="今年生日"><a href="#今年生日" class="headerlink" title="今年生日"></a>今年生日</h4><p>说小红this year的birthday是which day？.<br>I. It’s on May 26th,May 27th being Wednesday.<br>II. It’s not on Monday.<br>I only is sufficient。</p>
<h4 id="妹妹年龄"><a href="#妹妹年龄" class="headerlink" title="妹妹年龄"></a>妹妹年龄</h4><p>问妹妹今年多大啦？<br>I.妹妹比哥哥小xx岁<br>II.哥哥比妈妈小yy岁，妈妈zz年生的<br>I, II 加一起可以得出</p>
<h3 id="阅读理解"><a href="#阅读理解" class="headerlink" title="阅读理解"></a>阅读理解</h3><p>这是个阅读理解题。应当掌握托福阅读理解的技巧。<br>阅读理解中，错误选项的设置，无非是<br>无中生有<br>张冠李戴<br>以偏概全</p>
<p>所以此题的解题技巧就是，先确定句子成分，找出关键概念，关键概念间的关系。</p>
<h4 id="销售员问题"><a href="#销售员问题" class="headerlink" title="销售员问题"></a>销售员问题</h4><p>Sales drives in big organizations, many a times, fall flat on the face. A research showed that an average buyer remembers only 20% of the things discussed during a sales call.<br>The saddest part is that the sales team doesn’t get to choose what those 20% of things would be. The world today is cluttered with information and thus it is essential that the sales team represents their product/service in the best possible manner.<br>It is like answering questions that children ask. Expect and out of context questions and reply to each one of them, patiently, in a way that the customers understand the intricacies.<br>You can use technical terms to explain your product and its features. No doubt, it will be an accurate methodology but certainly not the right one.<br>Simplify your message and see how well your client remembers you and your presentation when you meet him to finally close the deal.</p>
<ol>
<li>A regular buyer would remember more than 20% of the details after a sales meeting</li>
<li>A customer is as gullible as a child and hence may ask many questions.</li>
<li>A better sales person would be the one who is able to explain the features of his/her product in a simple manner</li>
<li>If you simplify your message, the customer would remember your entire presentation.</li>
</ol>
<h4 id="印度公司问题"><a href="#印度公司问题" class="headerlink" title="印度公司问题"></a>印度公司问题</h4><p>It has been proven by research that in India, a company which purchases saturation radio advertising will get maximum brand recognition.<br>which option you can select:</p>
<ol>
<li>A high degree of brand recognition will help a company win a higher share of the market.</li>
<li>Radio has wide listenership and companies intending to increase their awareness,should advertise it.</li>
<li>For maximum brand recognition, a company need not spend on media channels other than radio publicizing.</li>
<li>Brand recognition in India is more heavily dependent on where the brand advertises than the quality of its offering.</li>
</ol>
<p>key conception: staturation advertising  &lt;—-&gt; brand recognition<br>relationship : maximun</p>
<p>A option, brand recopgnitino &lt;—&gt; share of the market. wrong 张冠李戴<br>B option, radio advertiseing increase their awareness. right<br>C option, not spend ohter than the radio.wrong. 无中生有<br>D option, Brand recognition &lt;—-&gt; brand advertisers , quality. 无中生有。</p>
<h4 id="科幻小说"><a href="#科幻小说" class="headerlink" title="科幻小说"></a>科幻小说</h4><p>有个fiction网站，是用来给科幻小说的读者来yy接下来桥段的，读者可以自己在上面续写科幻小说。比如哈利波特，如果哈利最开始没加入格兰芬多加入斯莱特林了呢？如果哈利没和好人做朋友而是成为马尔福集团的一份子了呢？<br>etc. 那么接下来剧情咋发展呢？有的作者觉得这个网站挺好的，因为可以受到启发，或者看看读者希望剧情如何发展。有的作者觉得这网站挺破的，因为你自己写故事为毛不自己新开一个坑写呢？而且还会干扰我思路。</p>
<ol>
<li>读科幻小说可以增加想象力。</li>
<li>这个网站有好有坏。 </li>
<li>网站上的同人使得原作黯然失色。</li>
<li>作者们都反对这个网站。<br>选 有好有坏.</li>
</ol>
<h4 id="气候与糖价"><a href="#气候与糖价" class="headerlink" title="气候与糖价"></a>气候与糖价</h4><p>说由于气候和糖的种植者积极性（因为糖价低，大家不爱种）的原因，很多人都去选择种jute了。最近四年糖价回升，并与jute价格持平了。问能推出什么：<br>a. 糖农会回来继续种糖<br>b. 糖价会继续攀升<br>其他两个答案肯定不对，不记得了。<br>这题我选的是糖农会回来种糖。后来发现应该是糖价继续攀升。因为跟jute同价格的话，不会吸引糖浓回来，只有糖价高于jute之后，糖农才会回来。</p>
<h4 id="电子邮件"><a href="#电子邮件" class="headerlink" title="电子邮件"></a>电子邮件</h4><p>现在员工都喜欢查看和及时回复email，说是上班时候也喜欢是不是看手机，这种行为影响了deadline, process啥的， 我选的选项是email has an adverse affect on performance</p>
<h4 id="motor效应"><a href="#motor效应" class="headerlink" title="motor效应"></a>motor效应</h4><p>说小孩和大人学习，会cooking，针线活什么的，叫做motor效应？实习精准的肌肉永远。简直完美~~~ 然后5个判断，选正确的。我选的是ride a biking也是motor</p>
<h4 id="真人秀"><a href="#真人秀" class="headerlink" title="真人秀"></a>真人秀</h4><p>真人秀 (答案： 参加的人通过做bizarre 的事情得到钱</p>
<h4 id="电视剧"><a href="#电视剧" class="headerlink" title="电视剧"></a>电视剧</h4><p>电视剧制作人总弄一种套路： 一个美女，一个 tranditional女（长相平庸之类的），争一个帅哥（hero），套路都是 帅哥先跟美女好，后来发现美女没有心灵美，traditional女有， 后来就跟t女好了结婚了。 因为creator知道masses大众喜欢story 有complexity 并且能challenge一下happy ending的套路。选项全忘了。容易选</p>
<h4 id="恩爱生活"><a href="#恩爱生活" class="headerlink" title="恩爱生活"></a>恩爱生活</h4><p>一男的周末喜欢在图书馆看书上网 他女票喜欢看 travel dramma 然后它们都爱运动 所以它们会一起去健身房， 晚上回来路上买蔬菜水果， 女的做饭男的在自己的library看书。 我选的选项是男的有一定数量的藏书。</p>
<h4 id="顾客所想"><a href="#顾客所想" class="headerlink" title="顾客所想"></a>顾客所想</h4><p>顾客不是很容易被操作，因为他们很清楚的知道别人跟他们想的不一样的。商店并不能get到顾客真正想要的</p>
<h4 id="课程表"><a href="#课程表" class="headerlink" title="课程表"></a>课程表</h4><p>排课表：有物理，化学，生物，然后有一些要求，问你能从哪些条件得出化学课排在哪一位，我选的是两个条件都要</p>
<h4 id="UFO"><a href="#UFO" class="headerlink" title="UFO"></a>UFO</h4><p>一个是讲ufo的，很多目击ufo的照片啥的都证明是假的，所以很多人说ufo不存在，<br>但很多科学家认为不能否认不存在，选项是虽然有些照片是假的,但不能说明ufo不存在。</p>
<h4 id="星球疑云"><a href="#星球疑云" class="headerlink" title="星球疑云"></a>星球疑云</h4><p>科学家在Z星球发现了干涸的河床！科学家推断（speculate), 当时Z星球上存在累死地球的，atmosphere ，absorb heat from sun，然后星球上发生了一次可以把 atmosphere taken away 的事件, 使星球变成了 vacuum 状态，annihilating life.<br>问这些可以infer to:，我选的atmosphere 是support life的必要前提条件.</p>
<h4 id="外星人"><a href="#外星人" class="headerlink" title="外星人"></a>外星人</h4><p>有一道有关外星人的题目，大致是有很多人声称见到过飞碟和外星人， 有人甚至拍了照片，但有很多照片被证明是自然现象或是飞机卫星， 最后说也有很多其他证据说明外星人的存在。<br>（我选的是最后 一个， 尽管有很多照片被证明是假的，但也不能否定外星人存在的 可能性）<br>Case A-信息不足 case B-满足</p>
<h4 id="炒鱿鱼"><a href="#炒鱿鱼" class="headerlink" title="炒鱿鱼"></a>炒鱿鱼</h4><p>Saira一直都是受同事们敬仰的一位好员工直到她因为bipola院合征带来的问题需要体假一段时间。不久后她就被炒鱿鱼了公司给出的理由是她的病情导致她工作效率低下并且会无意识地冒犯上级(bipoIar综合征的症状之一就是在无意识的情况下说各种话说个不停）。<br>而最终法院裁 定Salra被炒鱿鱼是因为公司相信了关于这种病的种种rn尹h（就是歧视）。问哪个选项是对的？（选 Saira被炒鱿鱼不是因为她自己有错其余几个选项都是空穴来风）l </p>
<h4 id="作家和配图"><a href="#作家和配图" class="headerlink" title="作家和配图"></a>作家和配图</h4><p>作家和网上配图什么的关系。 我选的是：这种行为对作家有好处也有坏处。</p>
<h3 id="阅读理解大题"><a href="#阅读理解大题" class="headerlink" title="阅读理解大题"></a>阅读理解大题</h3><h4 id="环保公司问题"><a href="#环保公司问题" class="headerlink" title="环保公司问题"></a>环保公司问题</h4><p>选择是否将候选公司放到一个环保list上，条件<br>1 have Environment Clearance Certificate ECC (一种认证)<br>2 developed at least 3 solar products.<br>3 none of their products are from synthetic<br>4 headquater in Texas<br>5 have a grade A certified unit of its products.<br>6 not have any legal dispute ralated to land or forest, pending against them<br>如果不满足2,但是有一种产品正在试验中:推荐给COO<br>如果不满足5:推荐给Director of the company</p>
<h4 id="录用-PM"><a href="#录用-PM" class="headerlink" title="录用 PM"></a>录用 PM</h4><p>一个公司要招PM，合理的candidate需满足以下条件:</p>
<ol>
<li>本科是学CS的</li>
<li>有MBA学位</li>
<li>本科GPA 3.0+</li>
<li>如果没有MBA学位，但是工作5年以上，需上报HR</li>
<li>本科不是学CS，但是在CS相关工作3年以上，上报HR<br>那么，请问:闰土本科学热水锅炉维修的，GPA 4.0，没有念过MBA，在 Google修了5年的锅炉，当了3年的程序员，则应该: D<br>A. 录用<br>B. 不录用<br>C. 条件不充分<br>D. 上报HR</li>
</ol>
<p>另一个条件:<br>1 候选人必须有硕士学位，且GPA为A<br>2 必须有两年以上工作经验，<br>3 若1不满足报告director 小明从事某工作三年，有CS和MBA，本科GPA为A-则:报告主管。<br>又一个条件条件是:<br>1 Master in commerce and at least B / have CPA 2 年龄大于20 ，小于25<br>3 流利的英语和西班牙语.<br>4 愿意付125刀押金<br>5 愿意承诺为公司工作5年<br>• 如果1不满足-&gt; refer to M director<br>• 如果4不满足 -&gt; refer to chair man .</p>
<h4 id="快递收费"><a href="#快递收费" class="headerlink" title="快递收费"></a>快递收费</h4><p>快递费要不要收的问题。条件是<br>1 地区code 大于10一类，小于10 另一类<br>2 商品价格超过500<br>3 不是deal的时候买得<br>4 之前没有bulk 超过5%的折扣.<br>5 客户有优良购买记录3年<br>• 如果不满足2，那么要是他满足地区code小于10，收10刀，大于10，收8刀。<br>• 如果不满足3，那么region code小于10，收5刀，大于10，收12刀<br>• 若不满足两条，则必须付全款。</p>
<p>来了一个老头，买了150刀的东西，不是deal的时候买的，也没有之前折扣。问 他可不可以不付运费。<br>选:不满足两条，2,3 附全款30刀</p>
<p>第二个case, Emma, 从ABC买了4年，没有bulk discount, area code 08, 上个月买了150的东西，有2%special discount, 有dealership, 加粗的不满足，也交30</p>
<p>The following are the details of the procedure of deciding delivery charges for goods bought from ABC company. </p>
<ol>
<li>The customers are divided into two categories: those who have sales region code of 10 or above into one category and those with a code</li>
<li>must have bought goods worth $500 or more in the previous month</li>
<li>must not have dealership of any other similar company.</li>
<li>must not have availed bulk discount before</li>
<li>must have been provided a special discount of 5% or less than that in the previous dealings</li>
<li>must have been regularly ordering for more than 3 years<br>however,</li>
<li>if the customer fulfills all the conditions except (2), and if the sales region code is less than 10, delivery charges of $10 would be levied. Delivery charges of $8 would be levied for a code more than 10</li>
<li>if the candidate fulfills all the conditions except (3), and if the sales region code is less than 10, deliver charges of $5 would be levied. Deliver charges of $12 would be levied for a code more than 10.</li>
<li>If the customer does not fulfill 2 or more of the conditions stated above, then he/she would have to pay delivery charges of $30 irrespective of the sales region.</li>
</ol>
<p>Q1. Jacob is a customer whose sales region code is 14. He had bought goods worth $150 from ABC company in June. He does not have dealership of any other similar company. He has never been provided any bulk discount or special discount.<br>A. He need not pay any delivery charges<br>B. He would have to pay $30 as delivery charges<br>C. has to pay $10<br>D. has to pay $8<br>E. Data insufficient</p>
<p>Q2. Emma is a customer whose sales region code is 08. She has been regularly ordering goods from ABC company for more than 4 years. She has also purchases goods worth $150 in the previous month. She has never been provided with any bulk discount, but has been given a special discount of 2%. However, she has dealership of some other similar company.<br>A. She need not pay any deliver charges<br>B. She would have to pay $30 as delivery charges<br>C. She has to pay $10<br>D. She has to pay $12<br>E. Data insufficient</p>
<h4 id="四人位置"><a href="#四人位置" class="headerlink" title="四人位置"></a>四人位置</h4><p>解题顺序：<br>step1: 先确定物体的位置，咖啡机和洗手间的和白板的位置。<br>step2: 再确定人的位置。</p>
<p>There are four coordinators named Lily, Cathy,Mary and Nina. Each coordinator is at a different corner of the rectangle meeting hall. A coffee vending machine is situated at one of the corners and a restroom at another corner of the meeting hall. Lily and Cathy are at either sides of the white board, which is situated at the center of the<br>side which is opposite to the side at whose corners the coffee vending machine and the restroom are located. Coordinator Mary is not at the corner where the restroom is located.</p>
<p>Q1. Which of the following cannot be true?<br>1 Lily is not on the side of the hall where the white board is placed<br>2 Nina is adjacent to the restroom at one corner<br>3 Cathy is at the corner, adjacent to the coffee vending machine.<br>4 Mary is adjacent to the coffee vending machine, at one corner of the hall 5 Lily is at the corner, adjacent to the coffee machine</p>
<p>Q2 which of the -hallowing pairs are at the diagonal corners .<br>Restroom and Nina<br>(Nina and Lily)<br>Mary and coffee vending machine<br>Cathy and Lily Nina and Mary </p>
<p>重点是这句“on either sides of the white board”，俩人分别在whiteboard的一侧， 而不是一定要在同一面hall的white board side.但是我觉得面经错了，L 和 C 必须再同一面墙上.<br>确定物体位置</p>
<figure class="highlight plain"><table><tr><td class="gutter"><pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br><span class="line">7</span><br><span class="line">8</span><br><span class="line">9</span><br><span class="line">10</span><br><span class="line">11</span><br><span class="line">12</span><br><span class="line">13</span><br><span class="line">14</span><br><span class="line">15</span><br><span class="line">16</span><br><span class="line">17</span><br><span class="line">18</span><br><span class="line">19</span><br><span class="line">20</span><br><span class="line">21</span><br><span class="line">22</span><br><span class="line">23</span><br><span class="line">24</span><br></pre></td><td class="code"><pre><span class="line">_________________________</span><br><span class="line">| ?                   ?(R)|</span><br><span class="line">| ||                      |</span><br><span class="line">| ||(W)                   |</span><br><span class="line">| ||                      |</span><br><span class="line">| ?__________________ ?(V)|</span><br><span class="line"></span><br><span class="line">确定人位置</span><br><span class="line">___________________________</span><br><span class="line">| C                   N(R)|</span><br><span class="line">| ||                      |</span><br><span class="line">| ||(W)                   |</span><br><span class="line">| ||                      |</span><br><span class="line">| L__________________ M(V)|</span><br><span class="line"></span><br><span class="line">题目里如果提到了 “at one corner”，比如2和4，应该就是说在Nina跟restroom在同一个角落</span><br><span class="line"></span><br><span class="line">错误:</span><br><span class="line">__________________________</span><br><span class="line">| N                   C(R)| </span><br><span class="line">| |                       |</span><br><span class="line">| |(W)                    |</span><br><span class="line">| |                       |</span><br><span class="line">| L__________________ M(V)|</span><br></pre></td></tr></table></figure>
<h4 id="八产品"><a href="#八产品" class="headerlink" title="八产品"></a>八产品</h4><p>A manufacture company has 8 products and 4 divisions. Four divisions are lead by Alan, Betty, Cathy, Diana. The 8 products are: mixer, iron, water pump, geyser, juicer, blender, grinder, and heater. Each division produces 2 products, no 2 divisions produces the same product. Diana’s division produced Geyser, Cathy’s division produces water pump. Mixer and iron areproduced by division lead by Alan and Betty respectively. The division that produces mixer doesn’t produce blender.<br>Four questions:</p>
<ol>
<li>if the division that produces mixer doesn’t produce juicer, which of the following statement is true?</li>
<li>if the division that produces mixer also produces juicer,how many ways are there for product pairs? (3! = 6)<br>For factory problems, take care of the global assumptions andl ocal assumptions.</li>
</ol>
<h4 id="出差问题"><a href="#出差问题" class="headerlink" title="出差问题"></a>出差问题</h4><p>说有M1,M2,M3,M4,M5和W1,W2,W3。出差必须派至少三男一女。M1和M3不能共存，M4和W2不能共存。<br>至少<br>第一问问如果派了M2和M3和W2，还可以派谁 (至少三男一女则M1和M4都不可能，所以M5, W1,W3)<br>第二问问如果M1 M2去了，还可以派谁。(M5W2W1W3,M4W1W3,M5M4W1W3)<br>第三问如果去了四个男生，那么谁不能选。(W2,因为M1和M3不能共存，则M4一定在，则W2不能在)</p>
<h4 id="圆桌问题"><a href="#圆桌问题" class="headerlink" title="圆桌问题"></a>圆桌问题</h4><p>圆桌问题解题技巧：<br>不同于房子顺序问题，圆桌问题没有初始化的下标.<br>setp1: 找相邻，将确定连续相邻的字母确定为初始下标。如例题一中的(AGE) 或者 (EGA) 定为 下标 1,2,3<br>step2: 找对面，可能对面的位置(1,5) (2,6) (3,7) (4,8), BH面对面,BH只可能是4,8 或8,4<br>step3: 找间隔，C?F, C和F之间只可能是D.</p>
<p>得出圆桌类型：<br>AGE B CDF H, AE可互换，BH可互换.</p>
<p>一圆桌坐八人ABCDEFGH. F在C右边两位,AE坐G两边, BH面对面:<br>• 问D对面是谁? G<br>• 以下哪两人坐对面? D&amp;G<br>• 谁坐D旁边? C<br>• AB不坐隔壁, F对面坐A, 反时针方向可能的坐法? EGA H CDF B</p>
<p> 八角桌， B和H正对着，F在C的右边两个位置，A 和E在G的两 侧，C朝北。</p>
<p>A, B, C, D, E, F, G, H are sitting around a round table. ‘F’ is two places to the right of ‘C’. ‘A’ and ‘E’ are on either side of ‘G’. ‘B’ and ‘H’ are opposite to each other. ‘C’ is facing north.<br>Q1 Who is sitting opposite to ‘D’ ? G<br>Q2 以下哪两人坐对面? D&amp;G.<br>Q3 谁坐D旁边? C.<br>Q4 which of the following arrangements (in anti-clockwise) is possible?<br>A  AGEBDCFH<br>B  AGEBCDHF<br>C  AGEBCDFH<br>D  ABFDCHEG</p>
<h4 id="团团坐，排排坐问题"><a href="#团团坐，排排坐问题" class="headerlink" title="团团坐，排排坐问题"></a>团团坐，排排坐问题</h4><p>6人团团坐问题，有六个人 GASMNR, 注意理解 G, A，S 两两不能对坐，所以总体来说分两种情况，GAS三人间隔而坐，或者GAS全都挨着坐。所有团团做的问题都围绕此基础展开。有<br>Q1. If R 在A S 中间，问你R对面是谁(G)。<br>Q2. if G左右是A R,问A 对面是谁(M or N)。<br>Q3. if NAR 连着坐， M两边是谁(S &amp; G).<br>Q4. if NAR 连着坐， A对面是谁（M）</p>
<p>说甲乙丙丁排排坐，甲在乙右边，丙在丁右边，能不能推断粗谁最右。（不能）</p>
<h4 id="七房间排序问题："><a href="#七房间排序问题：" class="headerlink" title="七房间排序问题："></a>七房间排序问题：</h4><p>七房间排序问题解题技巧：七房间排序问题，和圆桌问题的不同之处在于，圆桌是没有初始位置下标的。<br>step1: 找相邻，<br>step2: 找位置。<br>step3: 找间隔</p>
<p>有PQRSTUV7个房子，UP不能在2端，V在中间3个房子中的一个，TQ相邻，VR之间有2个，其中有一个是Q，QR不相邻，推测出位置就做出来，基于此题有4个问题。<br>VR之间有两个，Q在其中，TQ相邻，推出 VQTR，要注意取反, 或者 RTQV<br>V是中间三个房子中一个，决定了V一定在最中间,<br>又UP不能在两端，有一端必定是S.</p>
<p>S(UP)VQTR<br>RTQV(UP)S</p>
<p>UP可以互换</p>
<h4 id="石油公司招聘"><a href="#石油公司招聘" class="headerlink" title="石油公司招聘"></a>石油公司招聘</h4><p>Conditions for appointing a distributor, for petroleum gas throughout Georgia, are as follows. The applicant should:<br>Be an American by nationality<br>Be in the age group of 21-50 years as on 5th September, 2008<br>Be at least a high school graduate or any other recognized equivalent<br>Be a resident of Georgia. He/she should have stayed in Georgia for not less than 5 years, immediately preceding the date of application.<br>Have a family income of not more than $30,000 annually.<br>Not have dealership of any oil company<br>Not have any close relative as a dealer/distributor of any oil company<br>However,<br>Restrictions related to annual income would not be applicable to applicants working in corporations, owned or controlled by state departments. Such a case should be referred to the Managing Director<br>For unemployed applicants who hold at least a bachelor’s degree, conditions (6) and (7) may be waived<br>If an applicant is from a rural district but is not a resident of Georgia, the case may be referred to the Chairman.</p>
<p>Q1.William Trevino, who works in a public corporation owned by a state department, is an American by nationality. He is 23 years of age. He holds a bachelor’s degree and has an annual income of $35,000. He has been staying in Georgia for 7 years. Neither he nor any of his relatives works as a distributor or a dealer for any oil company.<br>He should be selected<br>He should not be selected<br>Insufficient data<br>The case should be referred to Managing Director<br>The case should be referred to the Chairman.<br>选Manager</p>
<p>Q2. Anna, a non-Georgia, American citizen, is a high school graduate with family income of $20,000 per annum. Her date of birth is 15.03.1985. she does not have dealership of any oil company nor des she has any close relative as a dealer or a distributor. She lives in a rural district.<br>She should be selected<br>She should not be selected.<br>Insufficient data.<br>The case should be referred to Managing Director.<br>The case should be referred to the Chairman<br>选Chairman</p>
<h4 id="招聘工程师"><a href="#招聘工程师" class="headerlink" title="招聘工程师"></a>招聘工程师</h4><p>An IT company has decided to recruit software developers. Conditions for selections of a candidate are as follows:<br>Should have at least a bachelor’s degree in engineering.<br>Should have scored at least 60% marks in his/her bachelor’s degree and 80% marks in 12th grade.<br>Must have at least 1 year’s work experience<br>Should be willing to sign a bond of 2 years.<br>Should not be more than 28 years and not less than 21 years of age as on 01.02.2012<br>However,<br>Candidates who fulfill all conditions except (1), but have obtained 75% in their bachelor’s degree (any computer applications degree like BCA) and have at least 3 years of work experience, may be referred to the Director<br>Who fulfill all conditions except (4), but are willing to pay an amount of $1000 as security deposit should be referred to the President<br>Who fulfill all conditions except (3), but are IT engineers may be referred to Deputy General Manager.<br>Alexander is an IT engineer with 65% marks in his bachelor’s degree and 88% marks in 12th grade. He completed his bachelor’s degree in engineer, in 2007 and immediately started working in a private firm. He is not ready to sign a bond but doesn’t mind paying a sum of $1000 as security deposit. He was 26 years old as on 01.01.2012<br>A He should not be recruited<br>B He should be recruited<br>C He should be referred to the President.<br>D He should be referred to the Deputy General Manager<br>E Data insufficient<br>小O，BCA 76%， 2年经验，不愿签两年bond，答案（直接拒了）</p>
<p>例题2.<br>挑候选人：条件是： </p>
<ol>
<li>Master in commerce and at least B / have CPA</li>
<li>年龄大于20 ，小于25</li>
<li>流利的英语和西班牙语. </li>
<li>愿意付125刀押金</li>
<li>愿意承诺为公司工作5年<br>除了1都满足-&gt; refer to Manager director.<br>除了4都满足 -&gt; refer to chairman .<br>23岁， 有CPA，懂SPANISH, ENGLISH， 愿意付100刀deposit， 愿意5年undertaking (to chairman)<br>Master, 成绩A， 懂SPANISH, ENGLISH， 愿意5年undertaking， ready to pay the required amount as deposit. 生日是01.11.1994 (ACCEPT)</li>
</ol>
<h4 id="比身高"><a href="#比身高" class="headerlink" title="比身高"></a>比身高</h4><p>有四个人R M K G(其实都有名字的，为了偷懒只记录了首字母)，哪个人最高？<br>给了两个条件：</p>
<ol>
<li>M 比G高，但是M比R矮</li>
<li>K比M高<br>（这两个条件加起来也得不出来）.</li>
</ol>
<h4 id="电商网站"><a href="#电商网站" class="headerlink" title="电商网站"></a>电商网站</h4><p>Buyme和INXsell两个卖东西的网站。区别是Buyme允许买卖二手。人们可以在上面卖book, bike, treadmill. 卖家设最低价，买家竞价，最后标得最高价的人必须买下，否则可以采取司法程序处理。但Buyme对于拍卖的物品没有保障。INXsell可以直接从生产商购买产品。<br>A. 两个网站都是online buying and selling 的web-portals.<br>B. buyme上仅仅可以拍卖book, bike, treadmill这几样二手物品。<br>C. 两个网站唯一区别是，Buyme允许买二手物品<br>D. buyme上出售的物品lowest price可以低至0<br>E. 竞得最高价的人必须要买下商品</p>
<p>选E</p>
<h4 id="公司分配住宿"><a href="#公司分配住宿" class="headerlink" title="公司分配住宿"></a>公司分配住宿</h4><p>条件：<br>1至少10年在公司工作工作其中至少4年是manager<br>2包括自己在内family人数不能超过5人<br>3以58岁为退体年龄至少还要工作5年才能退休<br>4没有自己的house<br>5不能住在配偶mate spouse的house里<br>6如果仅不满足1而且还是manager 的话上报给Finance Director<br>7如果仅不满足3而且还是senior manager的话上报给Manager Director<br>8如果是从外地搬来的可以不满足条件1<br>Q1 Jonh家里3个人,没有房子作为senior marager 4年,一共工作12年,2020年退休,问是否满足<br>Q2 老王家里3个人租房子住，作为manager 5年, 工作 11年，年龄42岁。<br>Q3 第二问那个女的没说家里有几个人，所以我选了信息不足，关键在于children，这是复数，可能有2个孩子，也可能有4个孩子。</p>
<h4 id="想要获得promotion，给出以下10个条件："><a href="#想要获得promotion，给出以下10个条件：" class="headerlink" title="想要获得promotion，给出以下10个条件："></a>想要获得promotion，给出以下10个条件：</h4><ol>
<li>至少工作5年</li>
<li>至少获得学士学位</li>
<li>写作成绩不低于60</li>
<li>Group discussion成绩不低于65</li>
<li>Interview成绩不低于 60</li>
<li>无犯罪记录</li>
<li>年龄在30～45岁之间</li>
<li>学术大于60. From 1point 3acres bbs</li>
<li>如果不满足3，而且group discussion成绩不低于75，interview不低于70，上报给general manager.</li>
<li>如果不满足8，上报给executive director</li>
</ol>

      
    </div>
    
    
    

    

    

    

    <footer class="post-footer">
      

      
      
      

      
        <div class="post-nav">
          <div class="post-nav-next post-nav-item">
            
              <a href="/2017/09/03/ReadingReview/For-the-sake-of-the-Republic-of-China/" rel="next" title="走向共和">
                <i class="fa fa-chevron-left"></i> 走向共和
              </a>
            
          </div>

          <span class="post-nav-divider"></span>

          <div class="post-nav-prev post-nav-item">
            
              <a href="/2017/09/06/Interview/Interview-Amazon-OA1-Debug/" rel="prev" title="Interview-Amazon-OA1-Debug">
                Interview-Amazon-OA1-Debug <i class="fa fa-chevron-right"></i>
              </a>
            
          </div>
        </div>
      

      
      
    </footer>
  </div>
  
  
  
  </article>



    <div class="post-spread">
      
    </div>
  </div>


          </div>
          


          

  
    <div class="comments" id="comments">
      <div id="disqus_thread">
        <noscript>
          Please enable JavaScript to view the
          <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a>
        </noscript>
      </div>
    </div>

  



        </div>
        
          
  
  <div class="sidebar-toggle">
    <div class="sidebar-toggle-line-wrap">
      <span class="sidebar-toggle-line sidebar-toggle-line-first"></span>
      <span class="sidebar-toggle-line sidebar-toggle-line-middle"></span>
      <span class="sidebar-toggle-line sidebar-toggle-line-last"></span>
    </div>
  </div>

  <aside id="sidebar" class="sidebar">
    
    <div class="sidebar-inner">

      

      
        <ul class="sidebar-nav motion-element">
          <li class="sidebar-nav-toc sidebar-nav-active" data-target="post-toc-wrap">
            Table of Contents
          </li>
          <li class="sidebar-nav-overview" data-target="site-overview-wrap">
            Overview
          </li>
        </ul>
      

      <section class="site-overview-wrap sidebar-panel">
        <div class="site-overview">
          <div class="site-author motion-element" itemprop="author" itemscope="" itemtype="http://schema.org/Person">
            
              <p class="site-author-name" itemprop="name">Wayne</p>
              <p class="site-description motion-element" itemprop="description"></p>
          </div>

          <nav class="site-state motion-element">

            
              <div class="site-state-item site-state-posts">
              
                <a href="/archives/">
              
                  <span class="site-state-item-count">615</span>
                  <span class="site-state-item-name">posts</span>
                </a>
              </div>
            

            
              
              
              <div class="site-state-item site-state-categories">
                <a href="/categories/index.html">
                  <span class="site-state-item-count">30</span>
                  <span class="site-state-item-name">categories</span>
                </a>
              </div>
            

            
              
              
              <div class="site-state-item site-state-tags">
                
                  <span class="site-state-item-count">10</span>
                  <span class="site-state-item-name">tags</span>
                
              </div>
            

          </nav>

          

          

          
          

          
          

          

        </div>
      </section>

      
      <!--noindex-->
        <section class="post-toc-wrap motion-element sidebar-panel sidebar-panel-active">
          <div class="post-toc">

            
              
            

            
              <div class="post-toc-content"><ol class="nav"><li class="nav-item nav-level-3"><a class="nav-link" href="#推理"><span class="nav-number">1.</span> <span class="nav-text">推理</span></a><ol class="nav-child"><li class="nav-item nav-level-5"><a class="nav-link" href="#字母推理"><span class="nav-number">1.0.1.</span> <span class="nav-text">字母推理</span></a></li><li class="nav-item nav-level-5"><a class="nav-link" href="#数字推理"><span class="nav-number">1.0.2.</span> <span class="nav-text">数字推理</span></a></li><li class="nav-item nav-level-5"><a class="nav-link" href="#间隔"><span class="nav-number">1.0.3.</span> <span class="nav-text">间隔</span></a><ol class="nav-child"><li class="nav-item nav-level-6"><a class="nav-link" href="#简单间隔"><span class="nav-number">1.0.3.1.</span> <span class="nav-text">简单间隔</span></a></li><li class="nav-item nav-level-6"><a class="nav-link" href="#按位间隔"><span class="nav-number">1.0.3.2.</span> <span class="nav-text">按位间隔</span></a></li><li class="nav-item nav-level-6"><a class="nav-link" href="#奇偶间隔"><span class="nav-number">1.0.3.3.</span> <span class="nav-text">奇偶间隔</span></a></li><li class="nav-item nav-level-6"><a class="nav-link" href="#递增间隔"><span class="nav-number">1.0.3.4.</span> <span class="nav-text">递增间隔</span></a></li></ol></li><li class="nav-item nav-level-5"><a class="nav-link" href="#平方-指数-反正就是2-n-3-n-4-n-n-2-n-3-n-4"><span class="nav-number">1.0.4.</span> <span class="nav-text">平方 指数 反正就是2^n, 3^n, 4^n ,n^2, n^3,n^4</span></a></li><li class="nav-item nav-level-5"><a class="nav-link" href="#求和，斐波拉契数列"><span class="nav-number">1.0.5.</span> <span class="nav-text">求和，斐波拉契数列</span></a></li></ol></li><li class="nav-item nav-level-4"><a class="nav-link" href="#递推表达式"><span class="nav-number">1.1.</span> <span class="nav-text">递推表达式</span></a><ol class="nav-child"><li class="nav-item nav-level-5"><a class="nav-link" href="#居然还有质数"><span class="nav-number">1.1.1.</span> <span class="nav-text">居然还有质数</span></a></li></ol></li></ol><li class="nav-item nav-level-3"><a class="nav-link" href="#排异题"><span class="nav-number">2.</span> <span class="nav-text">排异题</span></a></li><li class="nav-item nav-level-3"><a class="nav-link" href="#逻辑推理小题"><span class="nav-number">3.</span> <span class="nav-text">逻辑推理小题</span></a><ol class="nav-child"><li class="nav-item nav-level-4"><a class="nav-link" href="#自定义表达式。-这题一定要审题清楚，不能想当然。"><span class="nav-number">3.1.</span> <span class="nav-text">自定义表达式。 这题一定要审题清楚，不能想当然。</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#走路问题"><span class="nav-number">3.2.</span> <span class="nav-text">走路问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#楼层坐人问题"><span class="nav-number">3.3.</span> <span class="nav-text">楼层坐人问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#年龄问题"><span class="nav-number">3.4.</span> <span class="nav-text">年龄问题</span></a></li></ol></li><li class="nav-item nav-level-1"><a class="nav-link" href="#求日期"><span class="nav-number"></span> <span class="nav-text">求日期</span></a><ol class="nav-child"><li class="nav-item nav-level-4"><a class="nav-link" href="#排名问题"><span class="nav-number">0.1.</span> <span class="nav-text">排名问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#买车问题"><span class="nav-number">0.2.</span> <span class="nav-text">买车问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#球堆问题"><span class="nav-number">0.3.</span> <span class="nav-text">球堆问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#电离能"><span class="nav-number">0.4.</span> <span class="nav-text">电离能</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#买卖冰箱"><span class="nav-number">0.5.</span> <span class="nav-text">买卖冰箱</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#兴趣小组"><span class="nav-number">0.6.</span> <span class="nav-text">兴趣小组</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#哪天买车"><span class="nav-number">0.7.</span> <span class="nav-text">哪天买车</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#今年生日"><span class="nav-number">0.8.</span> <span class="nav-text">今年生日</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#妹妹年龄"><span class="nav-number">0.9.</span> <span class="nav-text">妹妹年龄</span></a></li></ol></li><li class="nav-item nav-level-3"><a class="nav-link" href="#阅读理解"><span class="nav-number">1.</span> <span class="nav-text">阅读理解</span></a><ol class="nav-child"><li class="nav-item nav-level-4"><a class="nav-link" href="#销售员问题"><span class="nav-number">1.1.</span> <span class="nav-text">销售员问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#印度公司问题"><span class="nav-number">1.2.</span> <span class="nav-text">印度公司问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#科幻小说"><span class="nav-number">1.3.</span> <span class="nav-text">科幻小说</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#气候与糖价"><span class="nav-number">1.4.</span> <span class="nav-text">气候与糖价</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#电子邮件"><span class="nav-number">1.5.</span> <span class="nav-text">电子邮件</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#motor效应"><span class="nav-number">1.6.</span> <span class="nav-text">motor效应</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#真人秀"><span class="nav-number">1.7.</span> <span class="nav-text">真人秀</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#电视剧"><span class="nav-number">1.8.</span> <span class="nav-text">电视剧</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#恩爱生活"><span class="nav-number">1.9.</span> <span class="nav-text">恩爱生活</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#顾客所想"><span class="nav-number">1.10.</span> <span class="nav-text">顾客所想</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#课程表"><span class="nav-number">1.11.</span> <span class="nav-text">课程表</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#UFO"><span class="nav-number">1.12.</span> <span class="nav-text">UFO</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#星球疑云"><span class="nav-number">1.13.</span> <span class="nav-text">星球疑云</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#外星人"><span class="nav-number">1.14.</span> <span class="nav-text">外星人</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#炒鱿鱼"><span class="nav-number">1.15.</span> <span class="nav-text">炒鱿鱼</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#作家和配图"><span class="nav-number">1.16.</span> <span class="nav-text">作家和配图</span></a></li></ol></li><li class="nav-item nav-level-3"><a class="nav-link" href="#阅读理解大题"><span class="nav-number">2.</span> <span class="nav-text">阅读理解大题</span></a><ol class="nav-child"><li class="nav-item nav-level-4"><a class="nav-link" href="#环保公司问题"><span class="nav-number">2.1.</span> <span class="nav-text">环保公司问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#录用-PM"><span class="nav-number">2.2.</span> <span class="nav-text">录用 PM</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#快递收费"><span class="nav-number">2.3.</span> <span class="nav-text">快递收费</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#四人位置"><span class="nav-number">2.4.</span> <span class="nav-text">四人位置</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#八产品"><span class="nav-number">2.5.</span> <span class="nav-text">八产品</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#出差问题"><span class="nav-number">2.6.</span> <span class="nav-text">出差问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#圆桌问题"><span class="nav-number">2.7.</span> <span class="nav-text">圆桌问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#团团坐，排排坐问题"><span class="nav-number">2.8.</span> <span class="nav-text">团团坐，排排坐问题</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#七房间排序问题："><span class="nav-number">2.9.</span> <span class="nav-text">七房间排序问题：</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#石油公司招聘"><span class="nav-number">2.10.</span> <span class="nav-text">石油公司招聘</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#招聘工程师"><span class="nav-number">2.11.</span> <span class="nav-text">招聘工程师</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#比身高"><span class="nav-number">2.12.</span> <span class="nav-text">比身高</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#电商网站"><span class="nav-number">2.13.</span> <span class="nav-text">电商网站</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#公司分配住宿"><span class="nav-number">2.14.</span> <span class="nav-text">公司分配住宿</span></a></li><li class="nav-item nav-level-4"><a class="nav-link" href="#想要获得promotion，给出以下10个条件："><span class="nav-number">2.15.</span> <span class="nav-text">想要获得promotion，给出以下10个条件：</span></a></li></ol></li></div>
            

          </div>
        </section>
      <!--/noindex-->
      

      

    </div>
  </aside>


        
      </div>
    </main>

    <footer id="footer" class="footer">
      <div class="footer-inner">
        <div class="copyright">&copy; <span itemprop="copyrightYear">2019</span>
  <span class="with-love">
    <i class="fa fa-user"></i>
  </span>
  <span class="author" itemprop="copyrightHolder">Wayne</span>

  
</div>


  <div class="powered-by">Powered by <a class="theme-link" target="_blank" href="https://hexo.io">Hexo</a></div>



  <span class="post-meta-divider">|</span>



  <div class="theme-info">Theme &mdash; <a class="theme-link" target="_blank" href="https://github.com/iissnan/hexo-theme-next">NexT.Mist</a> v5.1.4</div>




        







        
      </div>
    </footer>

    
      <div class="back-to-top">
        <i class="fa fa-arrow-up"></i>
        
      </div>
    

    

  </div>

  

<script type="text/javascript">
  if (Object.prototype.toString.call(window.Promise) !== '[object Function]') {
    window.Promise = null;
  }
</script>









  












  
  
    <script type="text/javascript" src="/lib/jquery/index.js?v=2.1.3"></script>
  

  
  
    <script type="text/javascript" src="/lib/fastclick/lib/fastclick.min.js?v=1.0.6"></script>
  

  
  
    <script type="text/javascript" src="/lib/jquery_lazyload/jquery.lazyload.js?v=1.9.7"></script>
  

  
  
    <script type="text/javascript" src="/lib/velocity/velocity.min.js?v=1.2.1"></script>
  

  
  
    <script type="text/javascript" src="/lib/velocity/velocity.ui.min.js?v=1.2.1"></script>
  

  
  
    <script type="text/javascript" src="/lib/fancybox/source/jquery.fancybox.pack.js?v=2.1.5"></script>
  


  


  <script type="text/javascript" src="/js/src/utils.js?v=5.1.4"></script>

  <script type="text/javascript" src="/js/src/motion.js?v=5.1.4"></script>



  
  

  
  <script type="text/javascript" src="/js/src/scrollspy.js?v=5.1.4"></script>
<script type="text/javascript" src="/js/src/post-details.js?v=5.1.4"></script>



  


  <script type="text/javascript" src="/js/src/bootstrap.js?v=5.1.4"></script>



  


  

    
      <script id="dsq-count-scr" src="https://weifeng.disqus.com/count.js" async></script>
    

    
      <script type="text/javascript">
        var disqus_config = function () {
          this.page.url = 'http://yoursite.com/2017/09/03/Interview/Interview-Amazon-OA1-Logic/';
          this.page.identifier = '2017/09/03/Interview/Interview-Amazon-OA1-Logic/';
          this.page.title = 'Interview-Amazon-OA1-Logic';
        };
        var d = document, s = d.createElement('script');
        s.src = 'https://weifeng.disqus.com/embed.js';
        s.setAttribute('data-timestamp', '' + +new Date());
        (d.head || d.body).appendChild(s);
      </script>
    

  




	





  














  

  <script type="text/javascript">
    // Popup Window;
    var isfetched = false;
    var isXml = true;
    // Search DB path;
    var search_path = "search.xml";
    if (search_path.length === 0) {
      search_path = "search.xml";
    } else if (/json$/i.test(search_path)) {
      isXml = false;
    }
    var path = "/" + search_path;
    // monitor main search box;

    var onPopupClose = function (e) {
      $('.popup').hide();
      $('#local-search-input').val('');
      $('.search-result-list').remove();
      $('#no-result').remove();
      $(".local-search-pop-overlay").remove();
      $('body').css('overflow', '');
    }

    function proceedsearch() {
      $("body")
        .append('<div class="search-popup-overlay local-search-pop-overlay"></div>')
        .css('overflow', 'hidden');
      $('.search-popup-overlay').click(onPopupClose);
      $('.popup').toggle();
      var $localSearchInput = $('#local-search-input');
      $localSearchInput.attr("autocapitalize", "none");
      $localSearchInput.attr("autocorrect", "off");
      $localSearchInput.focus();
    }

    // search function;
    var searchFunc = function(path, search_id, content_id) {
      'use strict';

      // start loading animation
      $("body")
        .append('<div class="search-popup-overlay local-search-pop-overlay">' +
          '<div id="search-loading-icon">' +
          '<i class="fa fa-spinner fa-pulse fa-5x fa-fw"></i>' +
          '</div>' +
          '</div>')
        .css('overflow', 'hidden');
      $("#search-loading-icon").css('margin', '20% auto 0 auto').css('text-align', 'center');

      $.ajax({
        url: path,
        dataType: isXml ? "xml" : "json",
        async: true,
        success: function(res) {
          // get the contents from search data
          isfetched = true;
          $('.popup').detach().appendTo('.header-inner');
          var datas = isXml ? $("entry", res).map(function() {
            return {
              title: $("title", this).text(),
              content: $("content",this).text(),
              url: $("url" , this).text()
            };
          }).get() : res;
          var input = document.getElementById(search_id);
          var resultContent = document.getElementById(content_id);
          var inputEventFunction = function() {
            var searchText = input.value.trim().toLowerCase();
            var keywords = searchText.split(/[\s\-]+/);
            if (keywords.length > 1) {
              keywords.push(searchText);
            }
            var resultItems = [];
            if (searchText.length > 0) {
              // perform local searching
              datas.forEach(function(data) {
                var isMatch = false;
                var hitCount = 0;
                var searchTextCount = 0;
                var title = data.title.trim();
                var titleInLowerCase = title.toLowerCase();
                var content = data.content.trim().replace(/<[^>]+>/g,"");
                var contentInLowerCase = content.toLowerCase();
                var articleUrl = decodeURIComponent(data.url);
                var indexOfTitle = [];
                var indexOfContent = [];
                // only match articles with not empty titles
                if(title != '') {
                  keywords.forEach(function(keyword) {
                    function getIndexByWord(word, text, caseSensitive) {
                      var wordLen = word.length;
                      if (wordLen === 0) {
                        return [];
                      }
                      var startPosition = 0, position = [], index = [];
                      if (!caseSensitive) {
                        text = text.toLowerCase();
                        word = word.toLowerCase();
                      }
                      while ((position = text.indexOf(word, startPosition)) > -1) {
                        index.push({position: position, word: word});
                        startPosition = position + wordLen;
                      }
                      return index;
                    }

                    indexOfTitle = indexOfTitle.concat(getIndexByWord(keyword, titleInLowerCase, false));
                    indexOfContent = indexOfContent.concat(getIndexByWord(keyword, contentInLowerCase, false));
                  });
                  if (indexOfTitle.length > 0 || indexOfContent.length > 0) {
                    isMatch = true;
                    hitCount = indexOfTitle.length + indexOfContent.length;
                  }
                }

                // show search results

                if (isMatch) {
                  // sort index by position of keyword

                  [indexOfTitle, indexOfContent].forEach(function (index) {
                    index.sort(function (itemLeft, itemRight) {
                      if (itemRight.position !== itemLeft.position) {
                        return itemRight.position - itemLeft.position;
                      } else {
                        return itemLeft.word.length - itemRight.word.length;
                      }
                    });
                  });

                  // merge hits into slices

                  function mergeIntoSlice(text, start, end, index) {
                    var item = index[index.length - 1];
                    var position = item.position;
                    var word = item.word;
                    var hits = [];
                    var searchTextCountInSlice = 0;
                    while (position + word.length <= end && index.length != 0) {
                      if (word === searchText) {
                        searchTextCountInSlice++;
                      }
                      hits.push({position: position, length: word.length});
                      var wordEnd = position + word.length;

                      // move to next position of hit

                      index.pop();
                      while (index.length != 0) {
                        item = index[index.length - 1];
                        position = item.position;
                        word = item.word;
                        if (wordEnd > position) {
                          index.pop();
                        } else {
                          break;
                        }
                      }
                    }
                    searchTextCount += searchTextCountInSlice;
                    return {
                      hits: hits,
                      start: start,
                      end: end,
                      searchTextCount: searchTextCountInSlice
                    };
                  }

                  var slicesOfTitle = [];
                  if (indexOfTitle.length != 0) {
                    slicesOfTitle.push(mergeIntoSlice(title, 0, title.length, indexOfTitle));
                  }

                  var slicesOfContent = [];
                  while (indexOfContent.length != 0) {
                    var item = indexOfContent[indexOfContent.length - 1];
                    var position = item.position;
                    var word = item.word;
                    // cut out 100 characters
                    var start = position - 20;
                    var end = position + 80;
                    if(start < 0){
                      start = 0;
                    }
                    if (end < position + word.length) {
                      end = position + word.length;
                    }
                    if(end > content.length){
                      end = content.length;
                    }
                    slicesOfContent.push(mergeIntoSlice(content, start, end, indexOfContent));
                  }

                  // sort slices in content by search text's count and hits' count

                  slicesOfContent.sort(function (sliceLeft, sliceRight) {
                    if (sliceLeft.searchTextCount !== sliceRight.searchTextCount) {
                      return sliceRight.searchTextCount - sliceLeft.searchTextCount;
                    } else if (sliceLeft.hits.length !== sliceRight.hits.length) {
                      return sliceRight.hits.length - sliceLeft.hits.length;
                    } else {
                      return sliceLeft.start - sliceRight.start;
                    }
                  });

                  // select top N slices in content

                  var upperBound = parseInt('1');
                  if (upperBound >= 0) {
                    slicesOfContent = slicesOfContent.slice(0, upperBound);
                  }

                  // highlight title and content

                  function highlightKeyword(text, slice) {
                    var result = '';
                    var prevEnd = slice.start;
                    slice.hits.forEach(function (hit) {
                      result += text.substring(prevEnd, hit.position);
                      var end = hit.position + hit.length;
                      result += '<b class="search-keyword">' + text.substring(hit.position, end) + '</b>';
                      prevEnd = end;
                    });
                    result += text.substring(prevEnd, slice.end);
                    return result;
                  }

                  var resultItem = '';

                  if (slicesOfTitle.length != 0) {
                    resultItem += "<li><a href='" + articleUrl + "' class='search-result-title'>" + highlightKeyword(title, slicesOfTitle[0]) + "</a>";
                  } else {
                    resultItem += "<li><a href='" + articleUrl + "' class='search-result-title'>" + title + "</a>";
                  }

                  slicesOfContent.forEach(function (slice) {
                    resultItem += "<a href='" + articleUrl + "'>" +
                      "<p class=\"search-result\">" + highlightKeyword(content, slice) +
                      "...</p>" + "</a>";
                  });

                  resultItem += "</li>";
                  resultItems.push({
                    item: resultItem,
                    searchTextCount: searchTextCount,
                    hitCount: hitCount,
                    id: resultItems.length
                  });
                }
              })
            };
            if (keywords.length === 1 && keywords[0] === "") {
              resultContent.innerHTML = '<div id="no-result"><i class="fa fa-search fa-5x" /></div>'
            } else if (resultItems.length === 0) {
              resultContent.innerHTML = '<div id="no-result"><i class="fa fa-frown-o fa-5x" /></div>'
            } else {
              resultItems.sort(function (resultLeft, resultRight) {
                if (resultLeft.searchTextCount !== resultRight.searchTextCount) {
                  return resultRight.searchTextCount - resultLeft.searchTextCount;
                } else if (resultLeft.hitCount !== resultRight.hitCount) {
                  return resultRight.hitCount - resultLeft.hitCount;
                } else {
                  return resultRight.id - resultLeft.id;
                }
              });
              var searchResultList = '<ul class=\"search-result-list\">';
              resultItems.forEach(function (result) {
                searchResultList += result.item;
              })
              searchResultList += "</ul>";
              resultContent.innerHTML = searchResultList;
            }
          }

          if ('auto' === 'auto') {
            input.addEventListener('input', inputEventFunction);
          } else {
            $('.search-icon').click(inputEventFunction);
            input.addEventListener('keypress', function (event) {
              if (event.keyCode === 13) {
                inputEventFunction();
              }
            });
          }

          // remove loading animation
          $(".local-search-pop-overlay").remove();
          $('body').css('overflow', '');

          proceedsearch();
        }
      });
    }

    // handle and trigger popup window;
    $('.popup-trigger').click(function(e) {
      e.stopPropagation();
      if (isfetched === false) {
        searchFunc(path, 'local-search-input', 'local-search-result');
      } else {
        proceedsearch();
      };
    });

    $('.popup-btn-close').click(onPopupClose);
    $('.popup').click(function(e){
      e.stopPropagation();
    });
    $(document).on('keyup', function (event) {
      var shouldDismissSearchPopup = event.which === 27 &&
        $('.search-popup').is(':visible');
      if (shouldDismissSearchPopup) {
        onPopupClose();
      }
    });
  </script><!-- hexo-inject:begin --><!-- Begin: Injected MathJax -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config("");
</script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i=0; i < all.length; i += 1) {
      all[i].SourceElement().parentNode.className += ' has-jax';
    }
  });
</script>

<script type="text/javascript" src="custom_mathjax_source">
</script>
<!-- End: Injected MathJax -->
<!-- hexo-inject:end -->





  

  

  

  
  

  
  


  

  

</body>
</html>

```

