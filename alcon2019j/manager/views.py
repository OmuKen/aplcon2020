from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
#manager.pyからデータ構造をimport
from manager.models import TB_Worker,TB_Skill,TB_VsSkill
from manager.forms import SkillSerchForm,SkillRegForm,WorkerRegForm,WorkerSkillRegForm
from django.db.models import Q



class HomeView(TemplateView):
  template_name = "home.html"
  def get(self, request, *args, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    #登録者数
    context['worker_num'] = TB_Worker.objects.count()
    #スキル数
    context['skill_num'] = TB_Skill.objects.count() 
    return render(self.request, self.template_name,context)

# Create your views here.
#ここでviewを作る
class WorkerListView(TemplateView):
 template_name = "worker_list.html"
 def get(self, request, *args, **kwargs):
    context = super(WorkerListView, self).get_context_data(**kwargs)

    #検索フォームに関する処理
    form = SkillSerchForm(self.request.GET or None)
    context['form'] = form
    
    if form.is_valid():
       #フォームから入力されたスキル名を取り出す
       skill_name = form.cleaned_data.get("skill_name")

       #skill_name=allが入力されたら全社員を表示する
       if skill_name == "all":
         s_worker = TB_VsSkill.objects.all().values_list('worker_code', flat=True).order_by('worker_code').distinct()
         context['select_worker'] = s_worker
         return render(self.request, self.template_name, context)

       context['skill_name'] = skill_name
       #スキル名に対応するスキルIDを取り出す(クエリの取り出しはできる)
       #スキル名の検索は完全一致(exact)で行う
       skill_code_Q = TB_Skill.objects.filter(Q(name__exact=skill_name))
      #一致するスキル名が存在しない時
       if skill_code_Q.first() == None:
         context['message'] = "スキルテーブルに一致するスキルが存在しません"
         return render(self.request, self.template_name, context)
       else:
         #クエリからスキルコードの抜き出し
         skill_code = skill_code_Q.get().skill_code
         context['skill_code'] = skill_code
         #htmlにはskill_codeに対応したTB_VsSkillのクエリセットを求める
         s_worker = TB_VsSkill.objects.filter(skill_code__skill_code=skill_code)
         context['select_worker'] = s_worker
         return render(self.request, self.template_name, context)

    else:
       return render(self.request, self.template_name, context)

#スキル登録画面
class SkillRegisterView(TemplateView):
  template_name = "skill_reg.html"

  def get(self, request, *args, **kwargs):
    context = super(SkillRegisterView, self).get_context_data(**kwargs)
    #登録フォーム
    form = SkillRegForm(self.request.GET or None)
    context['form'] = form

    if (form.is_valid()):
      skill_code = form.cleaned_data.get("code")
      skill_name = form.cleaned_data.get("name")
      #入力されたスキルコードかスキル名がTB_skillに存在するか調べる
      skill_code_Q = TB_Skill.objects.filter(Q(skill_code__exact=skill_code))
      skill_name_Q = TB_Skill.objects.filter(Q(name__exact=skill_name))
      if skill_code_Q.first() == None and skill_name_Q.first() == None:
        context['message'] = "スキル登録が完了しました"
        context['skill_code'] = skill_code
        context['skill_name'] = skill_name
        TB_Skill.objects.create(skill_code=skill_code, name=skill_name)
        return render(self.request, self.template_name, context)
      else:
        context['message'] = "そのスキルコードまたはスキル名はすでに登録済みです"
        context['skill_code'] = skill_code
        context['skill_name'] = skill_name
        return render(self.request, self.template_name, context)
      
    else:
      context['message'] = "有効なスキルコードを入力してください"
      return render(self.request, self.template_name, context)

#社員登録画面
class WorkerRegisterView(TemplateView):
  template_name = "worker_reg.html"

  def get(self, request, *args, **kwargs):
    context = super(WorkerRegisterView, self).get_context_data(**kwargs)
    #登録フォーム
    form = WorkerRegForm(self.request.GET or None)
    context['form'] = form
    if (form.is_valid()):
      worker_code = form.cleaned_data.get("code")
      #社員コードが登録済むか?
      worker_code_Q = TB_Worker.objects.filter(Q(worker_code__exact=worker_code))
      if worker_code_Q.first() == None:
        worker_name = form.cleaned_data.get("name")
        worker_dep = form.cleaned_data.get("dep")
        worker_mail = form.cleaned_data.get("mail")
        context['message'] = "社員登録が完了しました"
        TB_Worker.objects.create(worker_code=worker_code, name=worker_name,dep=worker_dep,mail=worker_mail)
        #DBに登録
        return render(self.request, self.template_name, context)
      else:
        context['message'] = "その社員コードは登録されています"
        return render(self.request, self.template_name, context)
    else:
      context['message'] = "有効な社員コードを入力してください"
      return render(self.request, self.template_name, context)

#社員スキル保有スキル登録画面
#スキルコードから、スキル名を逆引き⇨vsTableに登録する
class WorkerSkillRegisterView(TemplateView):
  template_name = "worker_skill_reg.html"
  def get(self, request, *args, **kwargs):
    context = super(WorkerSkillRegisterView, self).get_context_data(**kwargs)

    form = WorkerSkillRegForm(self.request.GET or None)
    context['form'] = form

    if (form.is_valid()):
      #formからデータを取得
      worker_code = form.cleaned_data.get("worker_code")
      skill_name = form.cleaned_data.get("skill_name")
      #入力されたスキルをDBのTB_Skillから検索し、クエリを取得
      TB_Skill_Q = TB_Skill.objects.filter(Q(name__exact=skill_name))
      #スキル表のスキル名が有る無し?
      if TB_Skill_Q.first() == None:
        context['message'] = "入力されたスキルは存在しません.スキル表にそのスキルを登録してください"
        return render(self.request, self.template_name, context)
      else:
        #社員が存在するかを調べていく
        TB_Worker_Q = TB_Worker.objects.filter(Q(worker_code__exact=worker_code))
        if TB_Worker_Q.first() == None:
          context['message'] = "入力された社員は存在しません"
          return render(self.request, self.template_name, context)
        else:
          #クエリからスキルコードを抜き出す
          skill_code = TB_Skill_Q.get().skill_code
          #worker_codeとskill_codeをTB_VsSkillに登録していく
          w = get_object_or_404(TB_Worker, worker_code=worker_code)
          s=get_object_or_404(TB_Skill, skill_code=skill_code)
          TB_VsSkill.objects.create(worker_code=w, skill_code=s)
          context['message'] = "スキル登録完了しました"
          return render(self.request, self.template_name, context)
    else:
      context['message'] = "社員コードとスキル名を入力してください"
      return render(self.request, self.template_name, context)

