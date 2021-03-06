
 /***************************************************************************
 *         Texture mapper by Dmitry Tjurev  (FidoNet 2:5061/15.49)          *
 *                 compile: wcc386                                          *
 ***************************************************************************/

  #define MNO_VERTS_IN_POLIGON 8    // ���ᨬ��쭮� ������⢮ ���設 � ��������
  #define MNO_SCAN_LINES 480        // ���ᨬ��쭮� ������⢮ ��ப ��࠭�

  typedef struct                    // ��ࠬ���� ������� ��।����� ��� 㪠��⥫� �� ⠪�� ��������
  {
    int   verts;                        // ������⢮ ���設 ��������
    float xt[MNO_VERTS_IN_POLIGON];     // ����࠭�⢥���
    float yt[MNO_VERTS_IN_POLIGON];     //                 ���न����
    float zt[MNO_VERTS_IN_POLIGON];     //                            ���設
    float xp[MNO_VERTS_IN_POLIGON];     // ��࠭�� ���न����
    float yp[MNO_VERTS_IN_POLIGON];     //                     ���設
    float xs[MNO_VERTS_IN_POLIGON];     // ⥪����� ���न����
    float ys[MNO_VERTS_IN_POLIGON];     //                       ���設
    float br[MNO_VERTS_IN_POLIGON];     // �મ�� � ���設��
    char  *texture;                     // 㪠��⥫� �� ⥪�����
  } face;

  void __memset(void *where,int what,int how_much);
  #pragma aux __memset parm [edi] [eax] [ecx]=\
    "cld"\
    "rep stosd"\
    modify exact[edi ecx];

  // ******** ( ����������� �� ���樠����樨 ) *******************

  int win_size_x,win_size_y;    // ࠧ��� �����-����
  char  *vid_buf;               // 㪠��⥫� �� �����-����
  char  color_tab[256*32];      // ⠡��� ��४���஢�� 梥�+类���=梥�
  int   *z_buf;                 // 㪠��⥫� �� Z-����
  double l_k;                   // ࠢ����� 0x7fffffff*(l-0.1), ��� l - ����ﭨ� �� ��࠭�

  // **************** �室�� ��ࠬ���� ****************************

  face *p;         // 㪠��⥫� �� �������� � �室�묨 ��ࠬ��ࠬ� ������

 //*****************  ����稥 ��६���� *******************

  int ypi[MNO_VERTS_IN_POLIGON];
  int zt_l[MNO_SCAN_LINES],zt_r[MNO_SCAN_LINES];
  int xpi_l[MNO_SCAN_LINES],xpi_r[MNO_SCAN_LINES];
  int xs_l[MNO_SCAN_LINES],ys_l[MNO_SCAN_LINES];
  int xs_r[MNO_SCAN_LINES],ys_r[MNO_SCAN_LINES];
  int br_l[MNO_SCAN_LINES],br_r[MNO_SCAN_LINES];

 //******************** ������� ������� **********************************

 void draw_spans(int line,int height)  // ���ᮢ�� ��१���
 {                                     // line - ��砫쭠� ��ப�
                                       // height - ����� ��ப
    int xsc,ysc,brc,ztc;                    // ⥪�騥 ���祭��
    int xs_add,ys_add,br_add,zt_add;        // ���饭��
    int x1,x2,len;
    int offs,offs2;

    offs=line*win_size_x;
m1: x1=xpi_l[line];
    x2=xpi_r[line];
    if ((x1>=win_size_x) || (x2<0)) goto m2;
    ztc=zt_l[line];
    xsc=xs_l[line];
    ysc=ys_l[line];
    brc=br_l[line];
    len=(x2-x1);
    if (len)
    {
      zt_add=(zt_r[line]-ztc)/len;
      xs_add=(xs_r[line]-xsc)/len;
      ys_add=(ys_r[line]-ysc)/len;
      br_add=(br_r[line]-brc)/len;
    }
    len++;
    if (x2>=win_size_x) len-=x2-win_size_x+1;
    if (x1<0)
    {
      len+=x1;
      ztc-=zt_add*x1;
      xsc-=xs_add*x1;
      ysc-=ys_add*x1;
      brc-=br_add*x1;
      x1=0;
    }
    offs2=offs+x1;
    do
    {
      if (ztc>z_buf[offs2])
      {
        z_buf[offs2]=ztc;
        vid_buf[offs2]=color_tab[((brc>>16)<<8)+*(p->texture+(xsc>>16)+((ysc>>16)<<8))];
      }
      offs2++;
      ztc+=zt_add;
      xsc+=xs_add;
      ysc+=ys_add;
      brc+=br_add;
    } while(--len);
m2: offs+=win_size_x;
    line++;
    if (--height) goto m1;
 }

  void scan_edge(int n1,int n2)  // ᪠��஢���� ॡ�
  {                              // x1,x2 - ����� ���設 ��砫� � ���� ॡ�
    int q,y,t;
    int xpc,xsc,ysc,brc,ztc;                  // ⥪�騥 ���祭��
    int xp_add,xs_add,ys_add,br_add,zt_add;   // ���饭��

    if (ypi[n1]>ypi[n2])
    {
      t=n1;
      n1=n2;
      n2=t;
    }
    y=ypi[n1];
    q=ypi[n2]-y;
    ztc=l_k/p->zt[n1];
    zt_add=(l_k/p->zt[n2]-ztc)/q;
    xpc=p->xp[n1]*65536;
    xsc=p->xs[n1]*65536;
    ysc=p->ys[n1]*65536;
    brc=p->br[n1]*65536;
    xp_add=((int)(p->xp[n2]*65536)-xpc)/q;
    xs_add=((int)(p->xs[n2]*65536)-xsc)/q;
    ys_add=((int)(p->ys[n2]*65536)-ysc)/q;
    br_add=((int)(p->br[n2]*65536)-brc)/q;
    q++;
    do
    {
      if (y<0) goto m1;
      if (y>=win_size_y) return;
      if ((xpc>>16) < xpi_l[y])
      {
        xpi_l[y]=xpc>>16;
        zt_l[y]=ztc;
        xs_l[y]=xsc;
        ys_l[y]=ysc;
        br_l[y]=brc;
      }
      if ((xpc>>16) > xpi_r[y])
      {
        xpi_r[y]=xpc>>16;
        zt_r[y]=ztc;
        xs_r[y]=xsc;
        ys_r[y]=ysc;
        br_r[y]=brc;
      }
m1:   ztc+=zt_add;
      xpc+=xp_add;
      xsc+=xs_add;
      ysc+=ys_add;
      brc+=br_add;
      y++;
    } while(--q);
  }

 void mapper()             // ᮡ�⢥���, ������
 {
   int q;
   int ymin,ymax;

   q=p->verts-1;
   do
   {
     ypi[q]=p->yp[q];
   } while(--q>=0);
   ymin=ymax=ypi[0];
   q=p->verts-1;
   do
   {
     if (ypi[q]<ymin) ymin=ypi[q];
       else
         if (ypi[q]>ymax) ymax=ypi[q];
   } while(--q);
   if ((ymin==ymax)||(ymin>=win_size_y)||(ymax<0)) return;
   if (ymin<0) ymin=0;
   if (ymax>=win_size_y) ymax=win_size_y-1;
   __memset(xpi_l+ymin,2100000000,ymax-ymin+1);
   __memset(xpi_r+ymin,-2100000000,ymax-ymin+1);
   q=p->verts-1;
   if (ypi[q]!=ypi[0]) scan_edge(q,0);
   q--;
   do if (ypi[q]!=ypi[q+1]) scan_edge(q,q+1);  while (--q>=0);
   draw_spans(ymin,ymax-ymin+1);
 }

